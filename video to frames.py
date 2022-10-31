import cv2
 
capture = cv2.VideoCapture('video_file_path') #change video_file_path
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'/frame_{frameNr}.jpg', frame) #change destination
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()