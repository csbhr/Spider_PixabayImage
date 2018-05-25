import RequestFunc
import FileFunc
import time
import requests
import os

# 根据关键字获取图片图片连接
def get_Image_Urls(word,pageNum):
    # 使用集合set存储连接，用于去重
    set_image_urls = set([])
    # 利用关键字word搜索图片，取1到5页图片
    image_detail_urls = RequestFunc.get_SearchPageWord_Image_DetailUrl(word, pageNum)
    for durl in image_detail_urls:
        image_url = RequestFunc.get_DetailPageUrl_Image_Url(durl)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + " >> Test : " + image_url)
        set_image_urls.add(image_url)
    return set_image_urls

# 负责业务的组织管理
def manage(word,pageNum):
    # 获取图片连接
    set_image_urls = get_Image_Urls(word,pageNum)
    print("KeyWord:" + word + " Get " + str(len(set_image_urls)) + " images.")

    # 将获取的连接存储到以关键字命名的文件中
    fileName = word +str(pageNum)+ ".txt"
    print("Write image urls into " + fileName + "......")
    FileFunc.writeTxt(fileName, set_image_urls)
    print("Write over......\n")

    # 将文件中存储的连接下载成文件
    set_image_urls = FileFunc.readTxt(fileName)
    # 以关键字创建目录
    dirName=word+str(pageNum)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    # 下载图片
    for url in set_image_urls:
        res = requests.get(url)
        imageName = dirName+"\\" + (url[30:]).replace("/", "&")
        print("Download " + imageName + "......")
        with open(imageName, "wb") as theFile:
            theFile.write(res.content)
        time.sleep(1)
    print("Download over.")
    print()
