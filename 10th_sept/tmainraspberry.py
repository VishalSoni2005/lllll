import time
import led_class
#import cam_class
import time
def change_cam(a):
    a[0],a[1],a[2],a[3]=a[3],a[0],a[1],a[2]
    return a
def change_lane(a):
    a[0],a[1],a[2],a[3]=a[3],a[0],a[1],a[2]
    return a

lane1 = led_class.LEDController(2,3,4,17)
lane2 = led_class.LEDController(27,22,23,24)
lane3 = led_class.LEDController(25,8,7,11)
lane4 = led_class.LEDController(19,26,16,20)
lanes = [lane1,lane2,lane3,lane4]

#cam1 = cam_class.cam_class(0)
#cam2 = cam_class.cam_class('https://192.168.0.107:8080/video')
#cam3 = cam_class.cam_class('https://192.168.0.103:8080/video')
#cam4 = cam_class.cam_class('https://192.168.0.101:8080/video')
#cam_lst = [cam1,cam2,cam3,cam4]

time_max = 400
time_min = 120
time_lane2 = 15
count = 0
lanes[1].on()
lanes[0].off()
lanes[2].off()
lanes[3].off()
time.sleep(1)
while count<10:
    count+=1
    #lanes[0].emer_on()
    #lanes[1].emer_on()
    #lanes[2].emer_on()
    #lanes[3].emer_on()
    print(count)
    lanes[2].off()
    time.sleep(0.5)
    lanes[3].off()
    time.sleep(0.5)
    #timer1 = timer.Timer(time_lane2)
    if lanes[1].is_on()==True:
        print(123)
    lanes[1].on(1)
    time.sleep(0.5)
    lanes[0].on(1)
    time.sleep(1)
    lanes[1].off()
    lanes[0].on()
    time.sleep(2)
    #car1 = cam_lst[0].count_car()
    #car2 = cam_lst[1].count_car()
    #car3 = cam_lst[2].count_car()
    #car4 = cam_lst[3].count_car()
    #print(car2)
    #print(car3)
    #print(car4)
    car2 = 5
    car3 = 10
    car4 = 6
    total_car = car2 + car3 + car4
    if total_car>30:
        time_per_lane = time_max//total_car
    elif total_car == 0:
        time_per_lane = 1
    else:
        time_per_lane = time_min//total_car
    #time_lane1 = time_per_lane*car1
    time_lane2 = max(time_per_lane*car2,5)
    time_lane3 = max(time_per_lane*car3,5)
    time_lane4 = max(time_per_lane*car4,5)
    #change_cam(cam_lst)
    print(time_lane2)
    change_lane(lanes)

print("Process Completed...")