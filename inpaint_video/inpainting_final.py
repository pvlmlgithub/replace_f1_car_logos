import subprocess
import cv2
import os

image_dir = 'input'
mask = 'mask/mask1.jpg'
output = 'output'

#video_path = 'video_input.mp4'
#cap = cv2.VideoCapture(video_path)

#fps = cap.get(cv2.CAP_PROP_FPS)
#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#os.makedirs(image_dir, exist_ok=True)

#image_count = 0

#while True:
#    ret, frame = cap.read()
#    if not ret:
#        break
#    image_count += 1
#    image_path = os.path.join(image_dir, f"frame_{image_count:04d}.jpg")
#    cv2.imwrite(image_path, frame)
#cap.release()

command = "iopaint run --model=lama --device=cuda --image={} --mask={} --output={}".format(image_dir,mask,output)
result = subprocess.run(command, shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print(result.stdout)
else:
    print("Error executing command:")
    print(result.stderr)
