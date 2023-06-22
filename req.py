import json
import base64
import requests
from datetime import datetime

# Submiting the POST Request for the Image
def submit_post(url: str, data: dict):
    return requests.post(url, data=json.dumps(data))


# Save Image with current time as name
def save_encoded_image(b64_image: str, output_folder: str):
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    output_path = f"{output_folder}/{current_datetime}.png"
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))


# Function to declare prompt, API-URL, etc.
if __name__ == '__main__':
    txt2img_url = 'http://127.0.0.1:7861/sdapi/v1/txt2img'
    data = {'prompt': 'ka Flagsharing'}
    response = submit_post(txt2img_url, data)
    save_encoded_image(response.json()['images'][0], 'output_folder')
