from ultralytics import YOLO
import cv2
import cvzone
import numpy as np
import math
import os

# Load YOLO model
model = YOLO("best.pt")
classNames = ["Helmet", "Mask", "Safety_Jacket"]

# --- Choose input file here ---
input_path = "3.jpg"  # change to "video.mp4" for video
output_path = "output.avi" if input_path.endswith(('.mp4', '.avi')) else "detection_output.jpg"

# Determine if input is image or video
is_video = input_path.lower().endswith((".mp4", ".avi", ".mov"))

# --- Image Mode ---
if not is_video:
    img = cv2.imread(input_path)
    results = model(img)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if conf > 0.1:
                color = (255, 0, 255) if currentClass == "Helmet" else (0, 255, 0)
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                cvzone.putTextRect(img, f'{currentClass} {conf:.2f}', (x1, max(35, y1)), scale=1, thickness=1, offset=2)

    cv2.imwrite(output_path, img)
    print(f"Saved result to {output_path}")

# --- Video Mode ---
else:
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

    frame_count = 0
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                currentClass = classNames[cls]

                if conf > 0.1:
                    color = (255, 0, 255) if currentClass == "Helmet" else (0, 255, 0)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cvzone.putTextRect(frame, f'{currentClass} {conf:.2f}', (x1, max(35, y1)), scale=1, thickness=1, offset=2)

        out.write(frame)
        frame_count += 1
        if frame_count % 10 == 0:
            print(f"Processed {frame_count} frames...")

    cap.release()
    out.release()
    print(f"Saved processed video to {output_path}")
