from git import Repo
import os
import requests
import re


class UploadManager:
    def __init__(self):
        self.ip = ['']
        self.path = '/home/van/AutoLoginUESTC/IPSendGithub'  # code的文件位置，我默认将其存放在根目录下

    def upload(self):
        # 访问http://myip.ipip.net获取当前公网ip，并写入ipaddress.txt文件
        try:
            res = requests.get('http://myip.ipip.net', timeout=5).text
            self.ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', res)
            self.ip = ['asd']
            print(self.ip)
            with open(os.path.join(self.path, 'ipaddress.txt'), 'w') as f:
                f.write(self.ip[0])
                print("ip获取写入成功")
        except:
            print("获取ip写入文件失败")

        # 上传git仓库到远程github
        try:
            repo = Repo(self.path)

            g = repo.git
            g.add("--all")
            g.commit("-m auto update")
            g.push()
            print("push github成功")
        except:
            print("push github错误")


if __name__ == '__main__':
    um = UploadManager()
    um.upload()
