# 🦺 Personal Protective Equipment Detection

A computer vision application to detect essential safety gear—**Helmet**, **Mask**, and **Safety Jacket**—in images and videos using a YOLOv8-based custom-trained model.

## 🚀 Features

- **Object Detection:** Identifies and labels safety equipment in images and videos.

- **Custom YOLO Model:** Trained specifically for detecting Helmet, Mask, and Safety Jacket.

- **Flexible Input:** Supports both image and video inputs.

- **Visual Output:** Annotated images/videos with bounding boxes and class labels.

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


