# python -m venv <env_name>
#source bitch/bin/activate
#sudo venv/bin/python3 -m pip install <package_name>

import cv2
import time
from ultralytics import YOLO

# Load the YOLO model
class yolo_cam_class:
    def __init__(self,video):
        self.video = video
    def count_car(self):
        model = YOLO("yolov10x.pt")

# Define custom label mapping
        custom_labels = {
            "car": "vehicle",
            "truck": "vehicle",
            "bus": "vehicle",
            "motorcycle": "vehicle",
            "bicycle": "vehicle",
            "cell phone": "vehicle"  # Rename cell phone to 'vehicle' as well
            }

        def count_vehicles(image):
            # Perform detection on the image
            results = model.predict(source=image, conf=0.2)  # Adjust confidence as needed
            total_objects_detected = 0

            for result in results:
                total_objects_detected += len(result.boxes)  # Add the number of detections

            return total_objects_detected

            # Step 1: Wait for 7 seconds before starting the camera
        time.sleep(1)

            # Step 2: Start the video capture (IP camera or webcam)
        cap = cv2.VideoCapture(self.video)  # Use 0 for webcam, or vpath for IP camera

        if not cap.isOpened():
            print("Error: Could not open video source")

                # Capture the frame quickly
        ret, frame = cap.read()

        if ret:
                    # Count vehicles within one second
            total_objects_webcam = count_vehicles(frame)
            print(f"Total vehicles: {total_objects_webcam}")

                    # Optionally display the frame  # Display the frame for 1 second

                # Release the camera after 1 second
            cap.release()
            cv2.destroyAllWindows()

            return total_objects_webcam
