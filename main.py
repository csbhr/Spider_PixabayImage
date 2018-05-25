import ManageFuc
import time

'''
# 用户循环输入关键字word，当用户输入exit使退出程序
word=input("Please input keyword:")
while word!="exit":
    ManageFuc.manage(word,1)
    word=input("Please input keyword:")

'''

list_word=["雨","龙卷风","云","地震","龙","神仙","西游","外星人","火影","海贼王"]
for word in list_word[3:]:
    for pageNum in range(1,9):
        ManageFuc.manage(word,pageNum)
        time.sleep(60)