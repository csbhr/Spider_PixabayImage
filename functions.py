import re
import requests
import html

def get_image_a_href_list(word):
    #搜索word页面的html
    url="https://pixabay.com/zh/photos/?q="+word+"&hp=&image_type=all&order=&cat=&min_width=&min_height="
    res=requests.get(url)
    body=html.unescape(res.text)
    #匹配图片详情页的url的正则表达式
    re_image_a_href=re.compile("<div class=\"item\" data-w=\".*?\" data-h=\".*?\"><a href=\"(.*?)\">",re.S)
    #匹配得到图片详情页的url列表
    list_image_a_href=re_image_a_href.findall(body)
    #返回url列表
    return list_image_a_href

def get_image_url_list_loop(list_image_a_href):
    i=0
    set_image_src=set([])
    re_image_src = re.compile("<img itemprop=\"contentURL\" srcset=\".*?\" src=\"(.*?)\" alt=\".*?\">", re.S)
    re_image_a_href = re.compile("<div class=\"item\" data-w=\".*?\" data-h=\".*?\"><a href=\"(.*?)\">", re.S)
    while i<len(list_image_a_href) and len(set_image_src)<30:
        href="https://pixabay.com/"+list_image_a_href[i]
        res=requests.get(href)
        body=html.unescape(res.text)
        #匹配到图片的url，并添加到集合
        src=re_image_src.findall(body)
        set_image_src.add(src[0])
        #print(src[0])
        #匹配到推荐的图片详情页的url列表，并添加到集合
        list_a_href=re_image_a_href.findall(body)
        for href in list_a_href:
            list_image_a_href.append(href)
        i=i+1
    return set_image_src

list_image_a_href=get_image_a_href_list("人物")
set_image_src=get_image_url_list_loop(list_image_a_href)
print(len(set_image_src))
for src in set_image_src:
    print(src)
