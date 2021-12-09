import cv2
import os


def process_video(video_path):
	video = cv2.VideoCapture(video_path)
	frame_rate = video.get(5)
	print('Video Frame Rate : {} FPS'.format(frame_rate))

	count = 0
	ignore = 5  # Drop Number of Frame

	while(video.isOpened()):
		for i in range(ignore):
			ret,frame=video.read()
		
		if ret:	
			#frame=cv2.resize(frame,(500,500))    # Resize if needed
			cv2.imwrite(output_dir+str(count)+'.jpg',frame)
			count += 1
			cv2.imshow('Frame',frame)
		key = cv2.waitKey(1)
		if key == ord('q'):
			break

	video.release()
	cv2.destroyAllWindows()
	print('Saved {} Images Successfully...'.format(count))



video_path = 'sample_video.mp4'    # path of video file
output_dir = './saved_frame/'

if os.path.isdir(output_dir):
	print('Folder Exists')
else:
	os.mkdir(output_dir)
	print('Output Folder Not exists, Creating {}'.format(output_dir))

if os.path.exists(video_path):
	process_video(video_path)

else:
	print('Video file {} not found, make sure it exists'.format(video_path))

