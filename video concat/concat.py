import cv2
import numpy as np


dir = '/home/aci/ACI Projects/GIT Projects/Person-Re-Identification/offline_data/'

video1 = cv2.VideoCapture(dir+'demo1.mp4')
print('Video1 Frame Rate : {} FPS'.format(video1.get(5)))
print('Video1 size : {} x {}'.format(video1.get(3), video1.get(4)))

video2 = cv2.VideoCapture(dir+'demo2.mp4')
print('Video2 Frame Rate : {} FPS'.format(video2.get(5)))
print('Video2 size : {} x {}'.format(video2.get(3), video2.get(4)))

resized_to = (1000,822)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('output.mp4', fourcc, 5.0, resized_to)


def padding_img(img, target_dim = (720,1280), color = (0, 0, 0), Fit_size=True):
    new_image_height, new_image_width = target_dim
    old_image_height, old_image_width, channels = img.shape

    h_ratio = new_image_height/old_image_height
    w_ratio = new_image_width/old_image_width
    
    if ((h_ratio<1) or (w_ratio<1)) and (not Fit_size):
        print('Target image dimension is smaller than input, Enabling Fit size option')
        Fit_size = True
        
    if Fit_size:
        fit_ratio = min(h_ratio,w_ratio)
        img = cv2.resize(img,(0,0), fx=fit_ratio, fy=fit_ratio)
        old_image_height, old_image_width, channels = img.shape
        
    result = np.full((new_image_height, new_image_width, channels), color, dtype=np.uint8)

    x_center = (new_image_width - old_image_width) // 2
    y_center = (new_image_height - old_image_height) // 2

    result[y_center:y_center+old_image_height, 
           x_center:x_center+old_image_width] = img

    return result

while video1.isOpened() and video2.isOpened():
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    
    if ret1 and ret2: 
        frame2 = padding_img(frame2, target_dim = (frame2.shape[0],frame1.shape[1]))
        vertical = np.concatenate((frame1, frame2), axis=0)
        out1.write(vertical)
        print(vertical.shape)
        cv2.imshow('F', vertical)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


out1.release()
cv2.destroyAllWindows()
print('Done')
