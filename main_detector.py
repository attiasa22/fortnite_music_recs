import cv2

# Load the video file
video_capture = cv2.VideoCapture("fortnitegameplay.mp4")

# Load the pre-trained pedestrian detection classifier
pedestrian_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

gun_cascade = cv2.CascadeClassifier('haarcascade_gun.xml')

# Loop through the frames of the video
i = 0
while True:
    # Read the next frame
    ret, frame = video_capture.read()
    # If there are no more frames, break out of the loop
    if not ret:
        break
    if i%5 ==0:
        # Convert the frame to grayscale
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect pedestrians in the frame
        pedestrians = pedestrian_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

        # Draw a rectangle around each detected pedestrian
        for (x, y, w, h) in pedestrians:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    if i%7 ==0:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect pedestrians in the frame
        guns = gun_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw a rectangle around each detected pedestrian
        for (x, y, w, h) in guns:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
quit
    # Wait for the user to press a key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    i += 1
# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()