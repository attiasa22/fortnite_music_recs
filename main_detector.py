import cv2
from helperfunctions import get_white_text, get_pixel_color
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
    if i%30 ==0:

        # Detect pedestrians in the frame
        pedestrians = pedestrian_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

        # Draw a rectangle around each detected pedestrian
        for (x, y, w, h) in pedestrians:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        shield = get_white_text(frame, 240, 400, 30,13)
        print("Shield: " + shield)
        health = get_white_text(frame, 235, 415, 30,20)
        print("Health: " + health)
        storm_time = get_white_text(frame, 694, 145, 30,20)
        print("Storm Time: " + storm_time)
        people_left = get_white_text(frame, 734, 145, 15,20)
        print("People Left: " + people_left)
        b,g,r = get_pixel_color(frame,690,160)
        
        if (b>150 and r>50 and g<20):
            print("STORM")
            print(b,g,r)
        else:
            print("NO STORM")
    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Wait for the user to press a key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    i += 1
    
# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()
