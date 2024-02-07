import cv2
import os

# Open the video file
video_path = 'test_removal.mp4'
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create the directory to save images if it doesn't exist
output_dir = 'input'
os.makedirs(output_dir, exist_ok=True)

# Counter for image filenames
image_count = 0

# Iterate through each frame in the video
while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    # Write the frame as an image
    image_count += 1
    image_path = os.path.join(output_dir, f"frame_{image_count:04d}.jpg")
    cv2.imwrite(image_path, frame)

# Release the video capture object
cap.release()

