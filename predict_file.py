from keras.layers import Input
from ssd import SSD
from PIL import Image
import os


ssd = SSD()
directory_name = 'C:\\Users\\Song1513675666666\\Desktop\\picture'
i=0
while i<=3:
    for filename in os.listdir(directory_name):
        img = directory_name + "/" + filename
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = ssd.detect_image(image)
            r_image.save('C:\\Users\\Song1513675666666\\Desktop\\picture1\\%s'%(filename))
            # r_image.show()     
        i+=1
            #将图片存放在当前目录
ssd.close_session()