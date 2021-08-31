import cv2
import time
import schedule
import random
from threading import Timer


start=time.time()
cap=cv2.VideoCapture(r"C:\Users\AQEEL\Desktop\Aqeel\sem-5\MP\sample videos\luci.mp4")
j=0
def job():
    j=random.randint(0,100)
    print("I'm working..aaa.")
    flag,frame=cap.read()
    cv2.imwrite('luci'+str(j)+'.jpg',frame)
    j=j+1
schedule.every(5).seconds.do(job)

while(cap.isOpened()):
    schedule.run_pending()





    



cap.release()
cv2.destroyAllWindows()
