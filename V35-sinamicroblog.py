import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from tqdm import tqdm
import re

host = 'm.weibo.cn'
base_url = 'https://%s/api/container/getIndex?' % host
user_agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/0.7.0 MicroMessenger/6.3.9 Language/zh_CN webview/0'

headers = {
    'Host': host,
    'Referer': 'https://m.weibo.cn/u/5495006460',
    'User-Agent': user_agent
}


# 按页数抓取数据
def get_single_page(page):
    params = {
        'type': 'uid',
        'value': 2649257207,
        'containerid': 1076032649257207,
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('抓取错误', e.args)


# 解析页面返回的json数据
def parse_page(json):
    items = json.get('data').get('cards')
    for item in items:
        item = item.get('mblog')
        if item:
            data = pq(item.get("text")).text()
            pics=item.get("pics")
            picList = []
            # 有些微博没有配图，所以需要加一个判断，方便后面遍历不会出错
            if pics is not None:
                for pic in pics:
                    pic_dict={}
                    pic_dict["pid"]=pic.get("pid")
                    pic_dict["url"]=pic.get("large").get("url")
                    picList.append(pic_dict)
            data = {
                'id': item.get('id'),
                'text': pq(item.get("text")),  # 仅提取内容中的文本
                'attitudes': item.get('attitudes_count'),
                'comments': item.get('comments_count'),
                'reposts': item.get('reposts_count')
            }
            yield data,picList

def imgDownload(results):
    """
    下载图片
    :param results:
    :return:
    """
    for result in results:
        for img_dict in result:
            img_name=img_dict.get("pid") + ".jpg"
            try:
                img_data=requests.get(img_dict.get("url")).content
                with open('/Users/violet/Downloads/屋内贵' + img_name, "wb") as file:
                    file.write(img_data)
                    file.close()
                    print(img_name + "\tdownload success!")
            except Exception as e:
                print(img_name + "\tdownload failed!", e.args)

def textdownload(results):
    '''
    下载文本
    :param results:
    :return:
    '''
    with open('/Users/violet/Downloads/xsy.txt', "a") as f:
        f.writelines(results)
        f.writelines('\n')
        f.close()

if __name__ == '__main__':
    for page in tqdm(range(1, 100)):  # 抓取前十页的数据
        json = get_single_page(page)
        results = parse_page(json)
        piclist = []
        textlist = []
        for result in results:
            text = str(result[0]['text'])
            info=''
            for n in range(0, len(text) - 1):
                if '\u4e00' <= text[n] <= '\u9fff' or text[n] in '：，,:0123456789.%':
                    info+=text[n]
            textdownload(info)
            # piclist.append(result[1])
        # imgDownload(piclist)

