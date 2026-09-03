import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Error: Could not open video stream from webcam")
    exit()

while True:
    ret, frame = cap.read()  
    if not ret:
        print("Error: Failed to capture frame from webcam")
        break
    
    
    results = model(frame)
    
    annotated_frame = results[0].plot()  # Draw bounding boxes and labels on the frame
    
    # Display the frame with predictions
    cv2.imshow('YOLOv8 Real-time Object Detection', annotated_frame)
    
    # Press 'q' to break the loop and quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
