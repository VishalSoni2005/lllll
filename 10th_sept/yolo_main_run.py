import yolo_cam_class
import time

a = yolo_cam_class.yolo_cam_class('https://192.168.0.107:8080/video')
b = yolo_cam_class.yolo_cam_class('https://192.168.0.107:8080/video')
c = yolo_cam_class.yolo_cam_class('https://192.168.0.107:8080/video')
d = yolo_cam_class.yolo_cam_class('https://192.168.0.107:8080/video')
count = 0
while count<2:
    print(a.count_car())
    count += 1