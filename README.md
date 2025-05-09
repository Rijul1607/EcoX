# EcoX: A Waste Segregator using YOLOv5

ECOX is an AI-powered waste segregation system that utilizes the YOLOv5 object detection model to classify and segregate waste into categories such as **plastic**, **metal**, **paper**, and **glass**. This project aims to promote efficient waste management by enabling real-time intelligent sorting.

---

## Demo 

https://github.com/user-attachments/assets/d5a1f132-ec8c-4f44-96bf-fefaf5146a6d

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

## 🧰 Tech Stack

### 🔧 Backend
- **Python** – Core programming language
- **Flask** – Lightweight web framework to serve the app

### 🧠 Machine Learning
- **YOLOv5** – Real-time object detection model for waste classification
- **PyTorch** – Deep learning framework used to train and run YOLOv5
- **OpenCV** – For image processing and camera feed handling
- **Pandas & NumPy** – Data handling and preprocessing

### 🌐 Frontend
- **HTML/CSS** – Basic user interface for the web app


### 🗃️ Other Tools
- **Jupyter Notebook** – For model training and experimentation
- **LabelImg / Roboflow** – For annotating the training dataset
- **Git & GitHub** – Version control and collaboration

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rijul1607/EcoX.git
   cd EcoX
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   ```


