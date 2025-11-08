import cv2

cap = cv2.VideoCapture(0)  # Open the webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Test', frame)  # Display webcam feed

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
