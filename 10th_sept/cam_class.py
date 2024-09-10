import cv2
import time

class cam_class:
    def __init__(self,video='video2.mp4'):
        self.video = video
    def count_car(self):
        haar_cascade = '/home/hp/trafficai/5th sept/Traffic-main/car1.xml'
        count = []
        detect = []
        offset = 6
        cap = cv2.VideoCapture(self.video)
        car_cascade = cv2.CascadeClassifier(haar_cascade)
        frame_count = 0
        def center_handle(x, y, w, h):
            cx = x + int(w / 2)
            cy = y + int(h / 2)
            return cx, cy

    # loop runs if capturing has been initialized.
        start = int(time.perf_counter())

        while frame_count<3:
        # reads frames from a video
            ret, frames = cap.read()
            cou = 0
            if not ret:
                return 0
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            cv2.line(frames, (25, 550), (1200, 550), (255, 127, 0), 2)
            if frame_count%30==0:
                for (x,y,w,h) in cars:
                    validate_count = (w >= 80) and (h >= 80)
                    if not validate_count:
                        continue
                    cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    center = center_handle(x, y, w, h)
                    detect.append(center)
                    cv2.circle(frames, center, 4, (0, 0, 255), -1)

                    for (x, y) in detect:
                        cou += 1
                        cv2.line(frames, (25, 550), (1200, 550), (0, 127, 255), 3)
                        detect.remove((x, y))
            count.append(cou)
            frame_count +=1
            # De-allocate any associated memory usage
            end_time = time.perf_counter()
            cv2.destroyAllWindows()
        return max(count)