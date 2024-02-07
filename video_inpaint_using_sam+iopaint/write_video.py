import cv2
import os

# Folder containing images
input_folder = 'output'

# Get the list of image filenames sorted in ascending order
image_files = sorted(os.listdir(input_folder))

# Read the first image to get its size
first_image = cv2.imread(os.path.join(input_folder, image_files[0]))
height, width, _ = first_image.shape

# Create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30  # Adjust the fps as needed
out = cv2.VideoWriter('video_output.mp4', fourcc, fps, (width, height))

# Iterate through each image and write it to the video
for image_file in image_files:
    # Read the image
    image_path = os.path.join(input_folder, image_file)
    frame = cv2.imread(image_path)

    # Write the frame to the output video
    out.write(frame)

# Release the VideoWriter object
out.release()
