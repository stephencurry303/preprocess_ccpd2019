import os #os：操作系统相关的信息模块
import random #导入随机函数
#存放原始图片地址
data_base_dir = "ccpd_out\\"
file_list = [] #建立列表，用于保存图片信息
#读取图片文件，并将图片地址、图片名和标签写到txt文件中
write_file_name = 'ccpd_base.txt'
write_file = open(write_file_name, "w") #以只写方式打开write_file_name文件
for file in os.listdir(data_base_dir): #file为current_dir当前目录下图片名
    if file.endswith(".jpg"): #如果file以jpg结尾
        write_name = file #图片路径 + 图片名 + 标签
        file_list.append(write_name) #将write_name添加到file_list列表最后
    sorted(file_list) #将列表中所有元素随机排列
    number_of_lines = len(file_list) #列表中元素个数
    #将图片信息写入txt文件中，逐行写入
for current_line in range(number_of_lines):
    write_file.write(file_list[current_line] + '\n')#关闭文件
