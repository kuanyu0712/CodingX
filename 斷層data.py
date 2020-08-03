import requests
import json
r = requests.get("https://www.geologycloud.tw/api/v1/zh-tw/Fault?t=.json", verify=False)
list_of_dicts = r.json()
print(r)
list_of_dicts=r.json()
list=[]
for i in list_of_dicts:
    for j in range(0,100,1):
        list=list+list_of_dicts['features'][j]['geometry']['coordinates']
print (list)