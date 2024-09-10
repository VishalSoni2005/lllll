# python -m venv <env_name>
#source bitch/bin/activate
#sudo venv/bin/python3 -m pip install <package_name>

import cv2
import time
from ultralytics import YOLO

# Load the YOLO model
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

while True:
    # Step 1: Wait for 7 seconds before starting the camera
    print("Waiting sec ...")
    time.sleep(3)
    vpath = 'http://192.168.0.107:8080/video'
    
    # Step 2: Start the video capture (IP camera or webcam)
    cap = cv2.VideoCapture(vpath)  # Use 0 for webcam, or vpath for IP camera

    if not cap.isOpened():
        print("Error: Could not open video source")
        break
    else:
        print(" 1sec ...")

        # Capture the frame quickly
        ret, frame = cap.read()

        if ret:
            # Count vehicles within one second
            total_objects_webcam = count_vehicles(frame)
            print(f"Total vehicles: {total_objects_webcam}")

            # Optionally display the frame
            # cv2.imshow("shw", frame)
    
            cv2.waitKey(2000)  # Display the frame for 1 second

        # Release the camera after 1 second
        cap.release()
        cv2.destroyAllWindows()
    
        print("...")
