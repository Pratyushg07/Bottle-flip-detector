# import cv2 as cv

# capture = cv.VideoCapture('flip.mp4')

# while True:
#     isTrue, frame = capture.read()
#     if not isTrue:
#         break
    
#     cv.imshow("flip.mp4", frame)
    
#     # Wait for key event for 20 milliseconds
#     key = cv.waitKey(20)
    
#     # Check if 'd' key is pressed
#     if key == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


# capture = cv.VideoCapture('flip.mp4')
# # Read the first frame
# isTrue, frame1= capture.read()

# if isTrue:
#     # Display the first frame as an image
   
#     cv.waitKey(0)  # Wait indefinitely for a key press
# else:
#     print("Failed to read the first frame.")
# cv.waitkey(200)
# capture.release()
# cv.destroyAllWindows()

import cv2 as cv

# Open the video file
capture = cv.VideoCapture('flip.mp4')

# Check if the video file was opened successfully
if not capture.isOpened():
    print("Error: Could not open video file.")
else:
    while True:
        # Read a frame
        isTrue, frame = capture.read()
        
        # Check if the frame was read successfully
        if not isTrue:
            break
        
        # Convert the frame to grayscale
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blurred_frame = cv.GaussianBlur(gray_frame, (5, 5), 0)
        # Apply Canny edge detection
        threshold ,thresh=cv.threshold(blurred_frame,185,200,cv.THRESH_BINARY)  # Adjust the thresholds as needed
        
        # Display the processed frame
        cv.imshow("Threshhold", thresh)
        
        # Check for key press to exit
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

    # Release the video capture resources
    capture.release()

# Close all OpenCV windows
cv.destroyAllWindows()




