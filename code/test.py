import cv2
import random


cap=cv2.VideoCapture(r"C:\Users\AQEEL\Desktop\Aqeel\sem-5\MP\sample videos\luci.mp4")
i=0
while(cap.isOpened()):
        
        print("I'm working..aaa..")
        flag,frame=cap.read()
        if flag==False:
            break            
        cv2.imwrite('luci'+str(i)+'.jpg',frame)
        i+=1

cap.release()
cv2.destroyAllWindows()
