import requests
import json
url = "https://api.imgbb.com/1/upload?key=d688272cbf7c207318520f5e3734f730"


def upload(image_base64):
    payload = {
        'image': image_base64
    }
    files = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response)
    data = json.loads(response.text)
    print(data['data']['url'])
    return data['data']['url']
