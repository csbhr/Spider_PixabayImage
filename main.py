import ManageFuc
import time


# 用户循环输入关键字word，当用户输入exit使退出程序
word=input("Please input keyword:")
while word!="exit":
    ManageFuc.manage(word)
    word=input("Please input keyword:")


'''
list_word=["山川","流水","树木","花草","田园","明星","模特","歌手","农民","工人","狗","猫","马","鸟","鱼","衣服","玩具","家具","房子","电器"]
for word in list_word[13:14]:
    ManageFuc.manage(word)
    time.sleep(5)
'''