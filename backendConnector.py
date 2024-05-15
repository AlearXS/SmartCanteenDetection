
import json
import requests
from getpass import getpass
headers = {"Authorization": "Basic QWRtaW46MTIzNDU2"} # Admin:123456
url = "http://127.0.0.1:8080/canteen"

def get(canteen_name: str):
    response = requests.get(url + '/' + canteen_name, headers=headers)
    if(response.status_code == 200):
        print('数据获取成功')
        print(response.json())
        return response.json()
    else:
        print('数据请求失败, 状态码：', response.status_code)
    # return 

def update(canteen_name: str, peopleNum: int):
    
    response = requests.patch(url + f'/{canteen_name}?peopleNum={peopleNum}', headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        print(f'成功更新 {canteen_name} {peopleNum}')
    else:
        print(f'Login failed with status code {response.status_code}')
        print(response.text)  # 打印响应内容以便于调试

if __name__ == "__main__":
    get('荷园一餐厅')
    update('荷园一餐厅', 3)
    get('荷园一餐厅')