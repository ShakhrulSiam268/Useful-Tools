import cv2
import numpy as np


video1 = cv2.VideoCapture('1.mkv')
print('Video1 Frame Rate : {} FPS'.format(video1.get(5)))
print('Video1 size : {} x {}'.format(video1.get(3), video1.get(4)))

video2 = cv2.VideoCapture('2.mp4')
print('Video2 Frame Rate : {} FPS'.format(video2.get(5)))
print('Video2 size : {} x {}'.format(video2.get(3), video2.get(4)))

resized_to = (1280, 720)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('out.mp4', fourcc, 40.0, resized_to)


def padd_img(img):
    old_image_height, old_image_width, channels = img.shape

    # create new image of desired size and color (blue) for padding
    new_image_width = 1280
    new_image_height = 720
    color = (0, 0, 0)
    result = np.full((new_image_height, new_image_width, channels), color, dtype=np.uint8)

    # compute center offset
    x_center = (new_image_width - old_image_width) // 2
    y_center = (new_image_height - old_image_height) // 2

    # copy img image into center of result image
    result[y_center:y_center+old_image_height, 
           x_center:x_center+old_image_width] = img

    return result


while video1.isOpened():
    ret, frame = video1.read()
    if ret: 
        out1.write(frame)
        cv2.imshow('F', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

while video2.isOpened():
    for i in range(2):
        ret, frame = video2.read()
    if ret: 
        frame = padd_img(frame)
        # frame=cv2.resize(frame,resized_to)
        out1.write(frame)
        print()
        cv2.imshow('F', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

out1.release()
cv2.destroyAllWindows()
print('Done')
