# 将txtList中的数据写入到文件fileName中
def writeTxt(fileName,txtList):
    with open(fileName,"w") as theFile:
        for line in txtList:
            theFile.write(line+"\n")


# 将文件fileName中数据读出，以list的形式返回
def readTxt(fileName):
    txtList=[]
    with open(fileName) as theFile:
        for line in theFile:
            txtList.append(line.strip())
    return txtList