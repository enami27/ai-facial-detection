import cv2

# load trained facial detection file 
cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)
if face_cascade.empty():
    raise ValueError("Failed to load the cascade classifier. Check the file path.")

# detect faces
def detect_faces(image):
    """ Detect faces in an image and draw rectangles around them """
    # grayscale image conversion for better detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect faces
    faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)

    # draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image

# capture input from default webcam
video_capture = cv2.VideoCapture(0)

while True:
    # frame by frame capture
    ret, frame = video_capture.read()
    if not ret:
        break

    # frame processing
    processed_frame = detect_faces(frame)

    # display result
    cv2.imshow('Video Face Detection', processed_frame)

    # if q is press = break frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release capture and close window
video_capture.release()
cv2.destroyAllWindows()
