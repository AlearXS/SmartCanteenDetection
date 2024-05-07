
import requests
from getpass import getpass
headers = {"Authorization": "Basic QWRtaW46MTIzNDU2"} # Admin:123456

def main():
    
    # 示例URL，替换为你需要访问的API地址
    url = "http://127.0.0.1:8080/monitoring"
    
    # 发送带有Authorization头的GET请求
    response = requests.patch(url + "?peopleNumber=123", headers=headers)
    if response.status_code == 200:
        print("认证成功，数据获取成功:")
        # print(response.json())
        breakpoint()
    else:
        print(f"认证失败，状态码: {response.status_code}")
	
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("认证成功，数据获取成功:")
        print(response.json())
    else:
        print(f"认证失败，状态码: {response.status_code}")

if __name__ == "__main__":
    main()