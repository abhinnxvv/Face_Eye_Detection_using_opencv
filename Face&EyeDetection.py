import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

cam_width = 1000
cam_height = 800

cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

# Define filter options
filters = {
    'Original': lambda img: img,
    'Grayscale': lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
    'Sepia': lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
}

current_filter = 'Original'

def apply_filter(frame):
    return filters[current_filter](frame)

def toggle_filter():
    global current_filter
    current_filter = next(iter(filters.keys()) - current_filter)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            cv2.putText(roi_color, 'Eye', (ex, ey - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)

    # Apply selected filter
    filtered_frame = apply_filter(frame)

    # Display filter option
    cv2.putText(filtered_frame, f'Filter: {current_filter}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Face & Eye Detection', filtered_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('f'):
        toggle_filter()

cap.release()
cv2.destroyAllWindows()
