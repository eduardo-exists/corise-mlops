import json
import requests
from tqdm import tqdm

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

def get_test_json():
    request_list = None

    with open('./data/requests.json', 'rb') as req_json:
        request_list = [json.loads(line) for line in req_json.readlines()]
    
    return request_list

def test_requests():
    for req_json in tqdm(get_test_json()):
        requests.post('http://0.0.0.0:80/predict', headers=headers, json=req_json)


if __name__ == '__main__':
    print('Tests Started')
    test_requests()
    print('Tests Completed')