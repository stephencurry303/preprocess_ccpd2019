import os
p="C:\CCPD2019\CCPD2019\ccpd_base\\"
data = os.listdir(p)
filename="C:\CCPD2019\CCPD2019\splits\\train.txt"
file = open(filename,'a')
for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
    s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
    file.write(s)
file.close()
print("保存文件成功")