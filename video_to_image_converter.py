import cv2

name='Siam'   # Person Name
url='./video_data/'+name+'.mp4'    # path of video file

video=cv2.VideoCapture(url)

count=0
ignr=5  # Drop frame
while(video.isOpened()):
	for i in range(ignr):
		try:
			ret,frame=video.read()
		except:
			pass
	#frame=cv2.resize(frame,(500,500))
	cv2.imwrite('./video_data/'+name+'/'+str(count)+'.jpg',frame)
	count += 1
	cv2.imshow('F',frame)
	key= cv2.waitKey(1)
	if key== 113:
		break

video.release()
cv2.destroyAllWindows()