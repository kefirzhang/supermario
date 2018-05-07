# coding=utf-8 ##以utf-8编码储存中文字符
"""
豆瓣高分电影top250信息采集
"""
import requests,bs4
#第一部分 豆瓣地址
url_list = [];
for i in range(10):
    cur_url = "https://movie.douban.com/top250?start="+str(i*25);
    url_list.append(cur_url)

#便利地址获取相应网页信息

movie_name_file = open('movie_name_file.txt','w+')
it = iter(url_list)
for address in it:
    res = requests.get(address)
    dom = bs4.BeautifulSoup(res.text,"html.parser")
    nodes = dom.select('.grid_view li')
    for node in nodes:
        title = node.select('.title')
        movie_name_file.write(title[0].text+"\n")
movie_name_file.close()

#第三部分存储对应信息  看看能不能存到数据库里面
