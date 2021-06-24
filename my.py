import cv2
import os

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

#车牌名字的对应
def getPlateNo(names):
    province = {0: "皖", 1: "沪", 2: "津", 3: "渝", 4: "冀", 5: "晋", 6: "蒙", 7: "辽", 8: "吉", 9: "黑", 10: "苏", 11: "浙",
                12: "京",
                13: "闽", 14: "赣", 15: "鲁", 16: "豫", 17: "鄂", 18: "湘", 19: "粤", 20: "桂", 21: "琼", 22: "川", 23: "贵",
                24: "云",
                25: "藏", 26: "陕", 27: "甘", 28: "青", 29: "宁", 30: "新"}
    plate_num = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "K", 10: "L", 11: "M",
                 12: "N",
                 13: "P", 14: "Q", 15: "R", 16: "S", 17: "T", 18: "U", 19: "V", 20: "W", 21: "X", 22: "Y", 23: "Z",
                 24: "0",
                 25: "1", 26: "2", 27: "3", 28: "4", 29: "5", 30: "6", 31: "7", 32: "8", 33: "9"}
    b = names.split("-")[4].split("_")
    plateNo = province[int(b[0])]
    for i in range(1, len(b)):
        plateNo = plateNo + plate_num[int(b[i])]
    return plateNo


root_dir = "C:\CCPD2019\CCPD2019\\"#根目录
root_files = ['ccpd_base','ccpd_blur', 'ccpd_db', 'ccpd_fn', 'ccpd_rotate', 'ccpd_tilt', 'ccpd_challenge','ccpd_weather','ccpd_np']

for root_file in root_files:
    root_path = os.path.join(root_dir, root_file)
    file_list = os.listdir(root_path)

    for names in file_list:
        img = cv2.imread(names)

        roi = cv2.rectangle(img, (getBiggerRec(names)[0], getBiggerRec(names)[1]),
                  (getBiggerRec(names)[2], getBiggerRec(names)[3]), (0, 0, 255), 1)

        AddText = img.copy()
        named_car_license = cv2.putText(AddText, getPlateNo(names), (getBiggerRec(names)[0], getBiggerRec(names)[1]),
                      cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 2)

        cv2.imshow(names, AddText)
        cv2.imwrite(named_car_license,roi)

        cv2.waitKey()
        cv2.destroyAllWindows()