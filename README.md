# EcoX: A Waste Segregator using YOLOv5

ECOX is an AI-powered waste segregation system that utilizes the YOLOv5 object detection model to classify and segregate waste into categories such as **plastic**, **metal**, **paper**, and **glass**. This project aims to promote efficient waste management by enabling real-time intelligent sorting.

---

## 🚀 Features

- 🔍 Real-time waste detection using YOLOv5
- ♻️ Classification into predefined waste categories
- 📷 Integration with camera or image input
- 📊 Option to log and visualize detected waste
- ⚡ Fast and efficient inference
- 🧠 Custom-trained YOLOv5 model for waste categories

---

## 📂 Project Structure

```plaintext
EcoX/
├── app.py                 # Main Flask application for web interface
├── model/
│   └── ecox_model.pt      # Trained YOLOv5 model weights
├── notebook/
│   └── EcoX_Training.ipynb # Jupyter notebook for training and evaluation
├── static/
│   └── ...                # Static assets like images, CSS
├── templates/
│   └── index.html         # Frontend HTML for the web UI
├── yolov5/                # YOLOv5 source code (add to .gitignore if not modifying)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Files and directories to ignore in Git

```

## 🧪 Dataset

You can get the dataset on this link https://universe.roboflow.com/material-identification/garbage-classification-3
