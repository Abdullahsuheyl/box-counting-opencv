import cv2
import numpy as np

video= cv2.VideoCapture("boxes.mp4")



background=cv2.createBackgroundSubtractorMOG2()
count= 0

while True:
    ret,frame= video.read()
    if ret:
        video1=cv2.resize(frame,(640, 480))
        video2=cv2.resize(frame,(640, 480))
        mask=background.apply(video2)


        
        cv2.line(video1,(180,240),(290,350),(0,0,255),2)
        cv2.line(video1,(210,230),(300,330),(0,0,255),2)
        
        contours,hierarchy =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try: hierarchy=hierarchy[0]
        except:hierarchy=[]
        for contour, hier in zip(contours,hierarchy):
            (x,y,w,h)=cv2.boundingRect(contour)
            if w>90 and h>90:
                cv2.rectangle(video1,(x,y),(x+w,y+h),(0,255,0),1)
                if y>230 and y<240:
                    count+=1
        cv2.putText(video1,"kutu: "+ str(count),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)


        cv2.imshow("Box Counting",video1)
        # cv2.imshow("Mask",mask)
        if cv2.waitKey(20) & 0xff ==ord("q"):
            break

video.release()
cv2.destroyAllWindows()


