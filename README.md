# 🦺 Personal Protective Equipment Detection

A computer vision application to detect essential safety gear—**Helmet**, **Mask**, and **Safety Jacket**—in images and videos using a YOLOv8-based custom-trained model.

## 🚀 Features

- 🔍 Real-time detection of PPE (Personal Protective Equipment)
- 🧠 YOLOv8 model trained on custom annotated dataset
- 📸 Works with both images and videos
- 💾 Saves visual output with bounding boxes and labels

## 📁 Project Structure

```
Safety-Kit-Detection/
├── labelled_images/    # Annotated training images
├── train/              # Training images
├── val/                # Validation images
├── best.pt             # Trained YOLO model weights
├── 1.jpeg, 2.jpeg     # Sample input images
├── custom_data.yaml    # Dataset config for YOLO
├── classes.txt         # Class labels
├── main.py             # Inference script (image/video)
└── README.md           # Project documentation
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Safety-Kit-Detection.git
cd Safety-Kit-Detection
```

2. Install required dependencies:
```bash
pip install ultralytics opencv-python pillow
```

## 🎯 Usage

### For Image Detection
```bash
python main.py --input 1.jpeg --type image
```

### For Video Detection
```bash
python main.py --input video.mp4 --type video
```

## 📊 Model Performance

The YOLOv8 model is trained to detect three classes:
- **Helmet** - Hard hats and safety helmets
- **Mask** - Face masks and respirators
- **Safety Jacket** - High-visibility vests and jackets

## 🏗️ Training Data

The model was trained on a custom dataset with annotated images containing various PPE scenarios in industrial and construction environments.

## 📝 Configuration

The `custom_data.yaml` file contains the dataset configuration:
- Training and validation paths
- Number of classes
- Class names

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- YOLOv8 by Ultralytics
- Custom dataset annotations
- Open source computer vision community
