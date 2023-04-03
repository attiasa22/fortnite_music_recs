import cv2
import pytesseract

def get_white_text(frame,x, y,w,h):
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cropped_img = frame[y:y+h,x:x+w]
    height,width, dim = cropped_img.shape
    dim = (width*10, height*10)
    cropped_img = cv2.resize(cropped_img,dim,cv2.INTER_AREA)
    # Convert the cropped image to grayscale
    gray_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    # Apply thresholding to enhance the text
    _, binary_img = cv2.threshold(gray_img, 170, 255, cv2.THRESH_BINARY_INV)

    #cv2.imshow('Video', binary_img)
    # Extract the text using pytesseract
    config_digit = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789:'
    return pytesseract.image_to_string(binary_img, config=config_digit)

def get_pixel_color(frame,x,y):

    b,g,r = (frame[y, x])
    cv2.rectangle(frame, (x-1, y-1), (x+1, y+1), (0, 0, 255), 1)
    #cv2.imshow('Video', frame[y-10:y+10,x-10:x+10])
    return  b,g,r 
    