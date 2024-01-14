import cv2
image = cv2.imread('pic.jpg')
x,y=46,214
width,height=758-x,694-y

src = image[y:y+height, x:x+width]
cv2.imwrite('src.jpg', src)
y=697
dest = image[y:y+height, x:x+width]
cv2.imwrite('dest.jpg', dest)

from PIL import Image
srcPil = Image.fromarray(src)
destPil = Image.fromarray(dest)
from PIL import ImageChops
diff = ImageChops.difference(srcPil, destPil)
diff.save('diff.jpg')

