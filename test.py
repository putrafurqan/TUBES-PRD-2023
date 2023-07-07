import cv2

# Read the video file
cap = cv2.VideoCapture('video3.mp4')

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Loop through the frames
while True:
    # Read a frame
    ret, frame = cap.read()
    
    # Check if frame read successfully
    if not ret:
        break
    
    # Show the frame
    cv2.imshow('Frame', frame)
    
    # Wait for 25 ms
    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video file and close all windows
cap.release()
cv2.destroyAllWindows()
