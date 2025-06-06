import requests
import os
import time
import html2text
import sys
import traceback
from bs4 import BeautifulSoup as bs
import re
import logging
from concurrent.futures import ThreadPoolExecutor
import hashlib
from time import gmtime, strftime

strdata=strftime("%D",gmtime()).replace('/','_')
logName=f'new_crawler{strdata}.log'

logging.basicConfig(filename=f'{logName}', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

def download_image(url, output_dir, filename, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                output_path = os.path.join(output_dir, filename)
                with open(output_path, "wb") as f:
                    f.write(response.content)
                return filename
            else:
                logging.error(f"Failed to download image: {url}")
        except Exception as e:
            logging.error(f"Error occurred while downloading image: {url}\n{e}")
            if i < retries - 1:  # i is zero indexed
                logging.info(f"Retrying...({i+1})")
                time.sleep(2)  # wait for 2 seconds before retrying
            else:
                logging.error(f"Failed to download image after {retries} attempts.")
    return None

def patch_fix_image_links(text, output_dir, title):
    # 正则表达式，用于匹配Markdown中的图像链接
    img_pattern = r'!\[[^\]]*\]\([^)]*\)'

    # 查找所有图片链接
    img_links = re.findall(img_pattern, text)

    # 遍历图片链接并修复换行符
    for img_link in img_links:
        fixed_img_link = img_link.replace('\n', '')
        text = text.replace(img_link, fixed_img_link)

        # 下载图片到指定目录
        img_url = re.search(r'\((.*?)\)', fixed_img_link).group(1)
        filename = f"{hashlib.md5(img_url.encode()).hexdigest()}.jpg"
        downloaded_filename = download_image(img_url, output_dir, filename, retries=3)

        if downloaded_filename:
            # 用相对路径替换图像链接
            year = time.strftime('%Y')
            month = time.strftime('%m')
            day = time.strftime('%d')
            relative_path = f"https://raw.githubusercontent.com/qqhsx/qqnews_image/main/{year}/{month}/{day}/{title}/{downloaded_filename}"
            text = text.replace(fixed_img_link, f"![{downloaded_filename}]({relative_path})")

    # 修复链接和文本显示在同行上的问题
    text = re.sub(r'(!\[[^\]]*\]\([^)]*\))(\n{1,2})?', r'\1\n\n', text)
    text = re.sub(r'(!\[[^\]]*\]\([^)]*\))(.)', r'\1\n\n\2', text)

    return text


def process_article(title, url):
    try:
        # 移除标题末尾的 "."
        title = sanitize_filename(title.rstrip('.'))

        tmphtml = requests.get(url).text
        tmpbs = bs(tmphtml, "html.parser")
        #ss = str(tmpbs.select("div.LEFT div.content.clearfix")[0])
        ss = str(tmphtml)
        ss = ss.replace("//inews.gtimg.com", "https://inews.gtimg.com").replace("</img>", "</img><br/>")
        ss = html2text.html2text(ss)
        #if len(ss.split()) <= 3:
            #logging.info(f"INVALID\n{title}\n{url}\n")
            #return

        year = time.strftime('%Y')
        month = time.strftime('%m')
        day = time.strftime('%d')
        output_dir = os.path.join(sys.path[0], year, month, day)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        img_dir = os.path.join("qqnews_image", year, month, day, title)

        if not os.path.exists(img_dir):
            os.makedirs(img_dir)

        # Fix image links and newline characters in Markdown file
        ss = patch_fix_image_links(ss, img_dir, title)

        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file = os.path.join(output_dir, f"{title}.md")
        if os.path.exists(output_file):
            logging.info(f"EXIST\n{title}\n{url}\n")
            return

        with open(output_file, "w", encoding="utf-8") as x:
            x.write(tmphtml)
        logging.info(f"SUCCESS\n{title}\n{url}\n{tmphtml}\n")
    except Exception as e:
        logging.error(f"ERROR\n{title}\n{url}\n{e.args}\n======\n{traceback.format_exc()}\n{tmphtml}\n")


def main():
    starttime = time.time()
    url1 = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=190&strategy=1&ext={"pool":["top","hot"],"is_filter":7,"check_type":true}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    qq1 = requests.get(headers=headers, url=url1).json()
     print(f"Total time taken: {qq1}")
    datalist = []
    for i in qq1["data"]["list"]:
        tmptitle = i["title"]
        tmpurl = i["url"]
        if time.strftime("%Y%m%d") not in tmpurl:
            logging.info(f"EXPIRED\n{tmptitle}\n{tmpurl}\n")
            continue
        datalist.append(tuple([tmptitle, tmpurl]))

    # Use thread pool to handle article download and processing
    with ThreadPoolExecutor(max_workers=5) as executor:
        for item in datalist:
            executor.submit(process_article, item[0], item[1])

    print(f"Total time taken: {time.time() - starttime} seconds")

if __name__ == '__main__':
    main()
