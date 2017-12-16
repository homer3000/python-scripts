'''
获取bing首页背景图，保存文件为2017-12-16_zh.jpg类似图片
依赖：python3
'''

from urllib.request import urlopen
from urllib.request import urlretrieve
from datetime import datetime

def get_background_image(url):
    is_en = url.find("ensearch") > -1
    now = datetime.now().strftime('%Y-%m-%d')
    filename = now + "_" + ("en" if is_en else "zh") + ".jpg"
    html = str(urlopen(url).read(), 'utf-8')
    start_idx = html.find("g_img={url: \"")
    end_idx = html.find(",", start_idx)
    image_url = "https://cn.bing.com" + html[start_idx + len("g_img={url: \""): end_idx - 1]
    now = datetime.now().strftime('%Y-%m-%d')
    urlretrieve(image_url, filename)
    print("get_background_image ok, filename=%s" % filename)


if __name__ == '__main__':
    get_background_image("https://cn.bing.com/?")
    get_background_image("https://cn.bing.com/?ensearch=1")
