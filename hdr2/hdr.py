import cv2
def gstreamer_pipeline():
        return (
        'v4l2src device=/dev/video3 ! '
        'video/x-raw, width=(int)1280, height=(int)720 ! '
        'videoconvert ! appsink')
    
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE,-1)


ret, frame = cap.read()

cv2.imwrite('640.jpg', frame)

cap.set(cv2.CAP_PROP_EXPOSURE,-3)


ret, frame = cap.read()

cv2.imwrite('160.jpg',frame)

cap.set(cv2.CAP_PROP_EXPOSURE,-6)


ret, frame = cap.read()

cv2.imwrite('20.jpg',frame)

