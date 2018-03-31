import RequestFunc
import FileFunc
import time

# 根据关键字获取图片图片连接
def get_Image_Urls(word):
    # 使用集合set存储连接，用于去重
    set_image_urls = set([])
    # 利用关键字word搜索图片，取1到10页图片
    for pageNumber in range(1, 11):
        image_detail_urls = RequestFunc.get_SearchPageWord_Image_DetailUrl(word, pageNumber)
        for durl in image_detail_urls:
            image_url = RequestFunc.get_DetailPageUrl_Image_Url(durl)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + " >> Test : " + image_url)
            set_image_urls.add(image_url)
    return set_image_urls

# 用户循环输入关键字word，当用户输入exit使退出程序
msg=input("Please input keyword:")
while msg!="exit":
    set_image_urls=get_Image_Urls(msg)
    print("KeyWord:"+msg+" Get "+str(len(set_image_urls))+" images.")
    # 将获取的连接存储到以关键字命名的文件中
    fileName=msg+".txt"
    print("Write image urls into "+fileName+"......")
    FileFunc.writeTxt(fileName, set_image_urls)
    print("Write over......\n")
    msg=input("Please input keyword:")
