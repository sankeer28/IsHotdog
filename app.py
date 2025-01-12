from flask import Flask, render_template, request, jsonify
import moondream as md
from PIL import Image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  
app.config['UPLOAD_FOLDER'] = 'temp_uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
model = md.vl(model="moondream-2b-int8.mf")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
MAX_IMAGE_SIZE = 512  

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def downscale_image(image):
    width, height = image.size
    if width > MAX_IMAGE_SIZE or height > MAX_IMAGE_SIZE:
        scale = MAX_IMAGE_SIZE / max(width, height)
        new_width = int(width * scale)
        new_height = int(height * scale)
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
        
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400
        
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        image = Image.open(filepath)
        processed_image = downscale_image(image)
        encoded_image = model.encode_image(processed_image)
        
        question = "Is this a hotdog? Please respond with yes if it is, and no if it isn't."
        response = model.query(encoded_image, question)["answer"]
        
        os.remove(filepath)
        
        is_hotdog = "yes" in response.lower()
        
        return jsonify({
            'model_response': response,
            'is_hotdog': is_hotdog
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)