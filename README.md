# IsHotdog 🌭

IsHotdog is a web application that determines whether an image contains a hotdog or not, inspired by the Silicon Valley TV show. It uses the Moondream-2B vision-language model for image classification.
![demo](https://github.com/user-attachments/assets/20ec709d-1328-4b5b-836b-b3717589f5b8)

## 🚀 Features

- Drag-and-drop or click-to-upload image interface
- Supports multiple image formats (JPG, JPEG, PNG, WEBP)
- Celebratory confetti animation for successful hotdog detection
- Responsive design with smooth animations
- Built with Flask and the [Moondream](https://github.com/vikhyat/moondream) model


1. Upload an image through the drag-and-drop interface or file browser
2. The image is processed and resized for efficiency
3. The Moondream model analyzes the image
4. The result is displayed with a visual indicator and the model's response
5. If it's a hotdog, celebrate with confetti! 🎉

📦 Installation

Clone the repository:
```
git clone https://github.com/sankeer28/IsHotdog.git
cd IsHotdog
```
Install the required Python packages:
```
pip install -r requirements.txt
```
[Install the moondream vision model](https://huggingface.co/vikhyatk/moondream2/resolve/9dddae84d54db4ac56fe37817aeaeb502ed083e2/moondream-2b-int8.mf.gz?download=true), add it to the IsHotdog folder


Run the application:
```
flask run
```
Open your browser and navigate to http://localhost:5000
