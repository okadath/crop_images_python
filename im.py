import glob
from PIL import Image
# read and crop image
# imm = Image.open('im/Screenshot from 2019-03-16 01-27-23.png')
# croppedIm = imm.crop((150, 120, 1210, 760))
# croppedIm.save('cropped2.png')

image_list = []
for filename in glob.glob('im/*.png'):
	image_list.append(filename)
image_list.sort()
# print(image_list)
i=0
for imsorted in image_list:
	#operations
	new_image=Image.open(imsorted)
	croppedIm = new_image.crop((150, 120, 1210, 760))
	#saving
	croppedIm.save('croped/'+str(i)+'.png')
	i=i+1
