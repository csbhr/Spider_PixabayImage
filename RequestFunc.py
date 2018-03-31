import re
import requests
import html

# 从搜索word得到的搜索界面获取图片的详情页连接
def get_SearchPageWord_Image_DetailUrl(word):
    # 获取html
    url = "https://pixabay.com/zh/photos/?q=" + word + "&hp=&image_type=all&order=&cat=&min_width=&min_height="
    res = requests.get(url)
    body = html.unescape(res.text)
    # 匹配图片详情页连接的正则表达式
    re_Image_DetailUrl = re.compile("<div class=\"item\" data-w=\".*?\" data-h=\".*?\"><a href=\"(.*?)\">", re.S)
    # 匹配得到图片详情页连接的列表
    list_Image_DetailUrl = re_Image_DetailUrl.findall(body)
    # 返回列表
    return list_Image_DetailUrl

# 从搜索连接得到的搜索界面获取图片的详情页连接
def get_SearchPageUrl_Image_DetailUrl(searchPageUrl):
    # 获取html
    res = requests.get("https://pixabay.com/"+searchPageUrl)
    body = html.unescape(res.text)
    # 匹配图片详情页连接的正则表达式
    re_Image_DetailUrl = re.compile("<div class=\"item\" data-w=\".*?\" data-h=\".*?\"><a href=\"(.*?)\">", re.S)
    # 匹配得到图片详情页连接的列表
    list_Image_DetailUrl = re_Image_DetailUrl.findall(body)
    # 返回列表
    return list_Image_DetailUrl

# 从图片的详情页获取图片的连接
def get_DetailPageUrl_Image_Url(detailPageUrl):
    # 获取html
    res = requests.get("https://pixabay.com/"+detailPageUrl)
    body = html.unescape(res.text)
    # 匹配图片连接的正则表达式
    re_Image_Url = re.compile("<img itemprop=\"contentURL\" srcset=\".*?\" src=\"(.*?)\" alt=\".*?\">", re.S)
    # 匹配得到图片连接
    list_Image_Url = re_Image_Url.findall(body)
    # 由于一个详情页只有一个图片，则返回列表第一个
    return list_Image_Url[0]

# 从图片的详情页提取拓展的搜索页连接
def get_DetailPageUrl_SeachPage_Url(detailPageUrl):
    # 获取html
    res = requests.get("https://pixabay.com/"+detailPageUrl)
    body = html.unescape(res.text)
    # 匹配搜索页连接的正则表达式
    re_SearchPage_Url = re.compile("<a href=\"(.*?)\">.*?</a> ", re.S)
    # 匹配得到搜索页连接
    list_SearchPage_Url = re_SearchPage_Url.findall(body)
    # 返回列表
    return list_SearchPage_Url
