import cv2 as cv
import cvzone
from ultralytics import YOLO
import math
import numpy as np

# Open the video file
cap = cv.VideoCapture('flip.mp4')
model = YOLO('yolov8l.pt')

classnames = []
with open('classes.txt', 'r') as f:
    classnames = f.read().splitlines()



# Read the first frame
ret, first_frame = cap.read()

if not ret:
    print("Error: Could not read the first frame.")
    exit()

# Process the first frame
detections = np.empty((0, 5))
results = model(first_frame, stream=True)
for info in results:
    parameters = info.boxes
    for box in parameters:
        x1, y1, x2, y2 = box.xyxy[0]
        
        confidence = box.conf[0]
        class_detect = box.cls[0]
        class_detect = int(class_detect)
        class_detect = classnames[class_detect]
        for bottle_box in info.boxes:
                    if classnames[int(bottle_box.cls[0])] == 'bottle':
                     x1, y1,x2,y2 = bottle_box.xyxy[0]
                     initial_y = y1

        conf = math.ceil(confidence * 100)
        if conf >= 60:
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv.rectangle(first_frame, (x1, y1), (x2, y2), (255, 0, 255), 5)
            cvzone.putTextRect(first_frame, f'{class_detect}', [x1 + 8, y1 - 12], scale=2, thickness=2, border=2)




final_y_bottle=initial_y
# Process the rest of the frames
while 1:
    flag=0
    ret, img = cap.read()

    if not ret:
        break

    detections = np.empty((0, 5))
    results = model(img, stream=True)

    for info in results:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            print(f'x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}')
            
            confidence = box.conf[0]
            class_detect = box.cls[0]
            class_detect = int(class_detect)
            class_detect = classnames[class_detect]
            old_y_bottle=final_y_bottle
            conf = math.ceil(confidence * 100)
            if conf >= 60:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 5)
                cvzone.putTextRect(img, f'{class_detect}', [x1 + 8, y1 - 12], scale=2, thickness=2, border=2)

                for bottle_box in info.boxes:
                    if classnames[int(bottle_box.cls[0])] == 'bottle':
                     x1, y1,x2,y2 = bottle_box.xyxy[0]
                     final_y_bottle = y1  # Assign y1 to final_y only for the bottle
                if old_y_bottle>final_y_bottle:
                        print("bottle started descending")
                         # Check if person is detected
                        for person_box in info.boxes:
                            if classnames[int(person_box.cls[0])] == 'person':
                                x1_person, y1_person, x2_person,y2_person = person_box.xyxy[0]
                                print(f"Person detected at ({x1_person}, {y1_person},{x2_person},{y2_person})")
                                if x1_person <x2 : 
                                    flag=1
                else:
                    continue 

                
                
    

    cv.imshow('frame', img)
    cv.waitKey(1)

# Release the video capture resources
cap.release()
cv.destroyAllWindows()

print(final_y_bottle)
print(initial_y)


cv.waitKey(100)
if initial_y- final_y_bottle <20:
            if flag==1:
                 print("cheating")
        
            else:
                 print("flip done")
else:
            print("Sorry")


