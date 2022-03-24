import cv2
trained_dataset = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)
while True:             
    success,frame=video.read()
    if success==True :
        gray_image= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = trained_dataset.detectMultiScale(gray_image)
        for x,y,w,h in faces:
            cv2.rectangle(frame , (x,y) ,(x+w,y+h),(255,0,0),2)
        cv2.imshow('video',frame)
        key=cv2.waitKey(1)
        if key =='d':
            break
    else:
        print('video completed or frame not found')
        break