import base64
import requests
# 导入环境变量
from dotenv import load_dotenv
import os

load_dotenv(override=True)
BASE_URL = os.getenv("MINIMAX_BASE_URL")
API_KEY = os.getenv("MINIMAX_API_KEY")
MODEL_ID = os.getenv("MINIMAX_MODEL_ID")

url = "https://api.minimax.cn/v1/image_generation"
api_key = API_KEY
headers = {"Authorization": f"Bearer {api_key}"}

payload = {
    "model": "image-01",
    "prompt": "画一张雄鹰展翅的图片，背景是绚丽的银河系，雄鹰上写着彩色的‘护道者’",
    "aspect_ratio": "16:9",
    "response_format": "base64",
}

response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()

images = response.json()["data"]["image_base64"]

for i in range(len(images)):
    with open(f"output-{i}.jpeg", "wb") as f:
        f.write(base64.b64decode(images[i]))