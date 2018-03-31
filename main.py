import RequestFunc
import FileFunc
import time
import sys

def get_Image_Urls(list_DetailUrl, list_Urls):
    if(len(list_Urls)>=2000):
        print("Distincting...")
        set_Urls = set(list_Urls)
        print("Get " + str(len(set_Urls)) + " Images.")
        print("Writing to urls.txt...")
        FileFunc.writeTxt("urls.txt", set_Urls)
        print("Writing over.")
        sys.exit(0)
    for durl in list_DetailUrl:
        imageUrl=RequestFunc.get_DetailPageUrl_Image_Url(durl)
        list_Urls.append(imageUrl)
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))+" >> Test Number"+str(len(list_Urls))+" : "+imageUrl)
    for durl in list_DetailUrl:
        extend_List_SearchUrl=RequestFunc.get_DetailPageUrl_SeachPage_Url(durl)
        extend_List_SearchUrl.sort()
        for elsurl in extend_List_SearchUrl:
            extend_List_DetailUrl=RequestFunc.get_SearchPageUrl_Image_DetailUrl(elsurl)
            get_Image_Urls(extend_List_DetailUrl,list_Urls)


list_DetailUrl=RequestFunc.get_SearchPageWord_Image_DetailUrl("风景")
list_Urls=[]
get_Image_Urls(list_DetailUrl,list_Urls)
print("Distincting...")
set_Urls=set(list_Urls)
print("Get "+str(len(set_Urls))+" Images.")
print("Writing to urls.txt...")
FileFunc.writeTxt("urls.txt", set_Urls)
print("Writing over.")