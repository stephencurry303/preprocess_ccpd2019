from PIL import Image

import matplotlib.pyplot as plt
img = Image.open("C:\Users\86176\PycharmProjects\carLicenseRecognition\ccpd_out\\01-86_91-298&341_449&414-458&394_308&410_304&357_454&341-0_0_14_28_24_26_29-124-24.jpg")
plt.imshow(img)
plt.show()
print(img.size)
img_crop = img.crop([img.size[0]/5,img.size[1]/5,img.size[0]*3/5,img.size[1]*3/5])
plt.imshow(img_crop)
plt.show()
