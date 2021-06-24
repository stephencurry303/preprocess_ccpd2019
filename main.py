# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import os
import numpy as np
import sys
from PIL import Image
#print(sys.stdin.encoding)
#print(sys.stdout.encoding)

provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "警", "学", "O"]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', 'O']
ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
       'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']

def rename_file(file):
    '''
    利用CCPD文件名获取车牌号码
    :param file: 文件名
    :return: 车牌号码
    '''
    filename_ = file.split('-')[4]
    filename_list = filename_.split('_')
    num_character = 0
    carid_list = list()
    for filename_split in filename_list:
        num_character += 1
        num = int(filename_split)
        #print(num)
        if num_character == 1:
            carid_list.append(provinces[num])
            print(carid_list)
        elif num_character == 2:
            carid_list.append(alphabets[num])
            print(carid_list)
        else:
            carid_list.append(ads[num])
            print(carid_list)
    name_renamed = ''.join(carid_list)
    return name_renamed

#得到车牌框
def getBiggerRec(names):
    b = names.split("-")[3].split("_")
    rb_x = int(b[0].split("&")[0])
    rb_y = int(b[0].split("&")[1])

    lb_x = int(b[1].split("&")[0])
    lb_y = int(b[1].split("&")[1])

    lu_x = int(b[2].split("&")[0])
    lu_y = int(b[2].split("&")[1])

    ru_x = int(b[3].split("&")[0])
    ru_y = int(b[3].split("&")[1])

    # 选最靠外的点
    return min(rb_x, lb_x, lu_x, ru_x), min(rb_y, lb_y, lu_y, ru_y), max(rb_x, lb_x, lu_x, ru_x), max(rb_y, lb_y, lu_y,
                                                                                                    ru_y)

dir = r"C:\Users\86176\PycharmProjects\carLicenseRecognition\ccpd_out\\"
carid_save_path = r"C:\CCPD2019\car_license\\"
name_list = os.listdir(dir)
for names in name_list:
    img = cv2.imread(dir + names)

    img_crop = img[getBiggerRec(names)[1]:getBiggerRec(names)[3],getBiggerRec(names)[0]:getBiggerRec(names)[2]]
    #cv2.imshow("cop",img_crop)
    AddText = img.copy()
    carid = rename_file(names)
    print(carid)
    suffix = '.jpg'
    image_name = '{}_{}'.format(carid, suffix)
    #cv2.imshow("roi",roi)
    save_path = os.path.join(carid_save_path, image_name)

    cv2.imwrite(save_path, img_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()


