import cv2
import os

cap = cv2.VideoCapture(0)

pathOut = 'detections'

count = 0       #count of the frames captured
avg = 0         #average value of all pixels in the frame
lastavg = 0     #comparison with the last average for detection

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    sum = 0

    lastavg = avg
    # Our operations on the frame come here
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rows = image.shape[0]
    cols = image.shape[1]

    #get sum of all pixel values
    for i in range(rows):
        for j in range(cols):
            k = image[i, j]
            sum = sum + k
            
    # get average of all the pixels meaning convert entire frame to one pixel
    
    avg = sum / (rows * cols)
    #print(avg)
    
    # changes in this pixel value is what will detect motion.
    avgDifference = lastavg - avg
    if avgDifference < 0:
        avgDifference = avgDifference * -1;

    #The lesser the threshold, the higher the detection sensitivity
    threshold = 2
    
    if (avgDifference > threshold):
        #print('Read %d frame: ' % count, ret)
        cv2.imwrite('detection'+str(count)+'.jpg',frame)
        # save frame as JPEG file
        count += 1

    # Display the resulting frame
    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
