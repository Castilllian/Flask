from flask import Flask, request
import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import aiohttp
import asyncio

app = Flask(__name__)

def download_image(url):
    response = requests.get(url)
    image_name = url.split('/')[-1]
    with open(image_name, 'wb') as file:
        file.write(response.content)
    return image_name

@app.route('/download', methods=['POST'])
def handle_download():
    urls = request.json.get('urls')
    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(download_image, urls))

    total_time = time.time() - start_time
    return {'images': results, 'total_time': total_time}

async def async_download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image_name = url.split('/')[-1]
            with open(image_name, 'wb') as file:
                file.write(await response.content.read())
            return image_name

@app.route('/download_async', methods=['POST'])
async def handle_async_download():
    urls = await request.json.get('urls')
    start_time = time.time()

    tasks = [asyncio.create_task(async_download_image(url)) for url in urls]
    results = await asyncio.gather(*tasks)

    total_time = time.time() - start_time
    return {'images': results, 'total_time': total_time}

if __name__ == '__main__':
    app.run()
