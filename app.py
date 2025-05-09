from flask import Flask, request, render_template, send_from_directory
import torch
from PIL import Image
import pathlib
import os

# Workaround for PosixPath error on Windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['OUTPUT_FOLDER'] = 'static/output'

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# Load the trained YOLOv5 model
def load_model():
    model_path = r'C:\Users\RIJUL GULATI\Documents\Custom Office Templates\OneDrive\Desktop\EcoX\yolov5'
    model = torch.hub.load(model_path, 'custom', source='local', 
                           path=r'C:\Users\RIJUL GULATI\Downloads\best.pt', 
                           force_reload=True)
    return model

model = load_model()

# Run inference on the image
def run_inference(image):
    # Run inference
    results = model(image)
    return results

# Flask routes
@app.route('/')
def home():
    return render_template('index.html')  # HTML file for image upload UI

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return render_template('index.html', error="No file uploaded")

    # Get the uploaded file
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error="No file selected")

    try:
        # Save the uploaded image
        uploaded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(uploaded_image_path)

        # Open the uploaded image using PIL
        img = Image.open(uploaded_image_path)

        # Convert image to RGB if necessary
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Run inference on the uploaded image
        results = run_inference(img)

        # Convert NumPy array to PIL.Image and save the processed image
        results_image = Image.fromarray(results.render()[0])
        output_image_path = os.path.join(app.config['OUTPUT_FOLDER'], 'output.jpg')
        results_image.save(output_image_path)

        # Get detected objects and ensure they are distinct
        detected_objects = list(set([model.names[int(cls)] for cls in results.xywh[0][:, -1].tolist()]))

        # Return results
        return render_template(
            'result.html',
            uploaded_image_url=uploaded_image_path.replace('static/', ''),
            output_image_url=output_image_path.replace('static/', ''),
            detected_objects=detected_objects
        )

    except Exception as e:
        return render_template('index.html', error=str(e))


# Serve static files
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
