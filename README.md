# 🦺 Personal Protective Equipment Detection

This application is designed to detect if people are wearing safety-jackets, hard-hats and a face mask. It's use cuts across different applications such as checking the safety complicance of workers on a site as to wearing their full safety gear(vest and helment) and also safety compliance of people wearing a face mask as a preventive measure due to the coronavirus or any other use case of a face mask.

## 🚀 Features

- **Object Detection:** Identifies and labels safety equipment in images and videos.

- **Custom YOLO Model:** Trained specifically for detecting Helmet, Mask, and Safety Jacket.

- **Flexible Input:** Supports both image and video inputs.

- **Visual Output:** Annotated images/videos with bounding boxes and class labels.

## 📁 Project Structure

```
Personal-Protective-Equipment-Detectionn/
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

## 🖼️ Output
![detection_output](https://github.com/user-attachments/assets/6911a0a6-9cbf-432d-afb2-eeb4373ef75b)



