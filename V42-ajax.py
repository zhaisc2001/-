import ssl
ssl._create_default_https_context=ssl._create_unverified_context

import requests
import re
import random

# １指定ajax-post请求的url（通过抓包进行获取）
url = 'https://m.wanplus.com/ajax/stats/list'

# 处理post请求携带的参数(从抓包工具中获取)
data = {
'_gtk' : 2087198897,
'draw' : 4,
'columns[0][data]' : 'order',
'columns[0][name]' : '',
'columns[0][searchable]' : 'true',
'columns[0][orderable]' : 'false',
'columns[0][search][value]' : '',
'columns[0][search][regex]' : 'false',
'columns[1][data]' : 'playername',
'columns[1][name]' : '',
'columns[1][searchable]' : 'true',
'columns[1][orderable]' : 'false',
'columns[1][search][value]' : '',
'columns[1][search][regex]' : 'false',
'columns[2][data]' : 'teamname',
'columns[2][name]' : '',
'columns[2][searchable]' : 'true',
'columns[2][orderable]' : 'false',
'columns[2][search][value]' : '',
'columns[2][search][regex]' : 'false',
'columns[3][data]' : 'meta',
'columns[3][name]' : '',
'columns[3][searchable]' : 'true',
'columns[3][orderable]' : 'false',
'columns[3][search][value]' : '',
'columns[3][search][regex]' : 'false',
'columns[4][data]' : 'appearedTimes',
'columns[4][name]' : '',
'columns[4][searchable]' : 'true',
'columns[4][orderable]' : 'true',
'columns[4][search][value]' : '',
'columns[4][search][regex]' : 'false',
'columns[5][data]' : 'kda',
'columns[5][name]' : '',
'columns[5][searchable]' : 'true',
'columns[5][orderable]' : 'true',
'columns[5][search][value]' : '',
'columns[5][search][regex]' : 'false',
'columns[6][data]' : 'attendrate',
'columns[6][name]' : '',
'columns[6][searchable]' : 'true',
'columns[6][orderable]' : 'true',
'columns[6][search][value]' : '',
'columns[6][search][regex]' : 'false',
'columns[7][data]' : 'killsPergame',
'columns[7][name]' : '',
'columns[7][searchable]' : 'true',
'columns[7][orderable]' : 'true',
'columns[7][search][value]' : '',
'columns[7][search][regex]' : 'false',
'columns[8][data]' : 'mostkills',
'columns[8][name]' : '',
'columns[8][searchable]' : 'true',
'columns[8][orderable]' : 'true',
'columns[8][search][value]' : '',
'columns[8][search][regex]' : 'false',
'columns[9][data]' : 'deathsPergame',
'columns[9][name]' : '',
'columns[9][searchable]' : 'true',
'columns[9][orderable]' : 'true',
'columns[9][search][value]' : '',
'columns[9][search][regex]' : 'false',
'columns[10][data]' : 'mostdeaths',
'columns[10][name]' : '',
'columns[10][searchable]' : 'true',
'columns[10][orderable]' : 'true',
'columns[10][search][value]' : '',
'columns[10][search][regex]' : 'false',
'columns[11][data]' : 'assistsPergame',
'columns[11][name]' : '',
'columns[11][searchable]' : 'true',
'columns[11][orderable]' : 'true',
'columns[11][search][value]' : '',
'columns[11][search][regex]' : 'false',
'columns[12][data]' : 'mostassists',
'columns[12][name]' : '',
'columns[12][searchable]' : 'true',
'columns[12][orderable]' : 'true',
'columns[12][search][value]' : '',
'columns[12][search][regex]' : 'false',
'columns[13][data]' : 'goldsPermin',
'columns[13][name]' : '',
'columns[13][searchable]' : 'true',
'columns[13][orderable]' : 'true',
'columns[13][search][value]' : '',
'columns[13][search][regex]' : 'false',
'columns[14][data]' : 'lasthitPermin',
'columns[14][name]' : '',
'columns[14][searchable]' : 'true',
'columns[14][orderable]' : 'true',
'columns[14][search][value]' : '',
'columns[14][search][regex]' : 'false',
'columns[15][data]' : 'damagetoheroPermin',
'columns[15][name]' : '',
'columns[15][searchable]' : 'true',
'columns[15][orderable]' : 'true',
'columns[15][search][value]' : '',
'columns[15][search][regex]' : 'false',
'columns[16][data]' : 'damagetoheroPercent',
'columns[16][name]' : '',
'columns[16][searchable]' : 'true',
'columns[16][orderable]' : 'true',
'columns[16][search][value]' : '',
'columns[16][search][regex]' : 'false',
'columns[17][data]' : 'damagetakenPermin',
'columns[17][name]' : '',
'columns[17][searchable]' : 'true',
'columns[17][orderable]' : 'true',
'columns[17][search][value]' : '',
'columns[17][search][regex]' : 'false',
'columns[18][data]' : 'damagetakenPercent',
'columns[18][name]' : '',
'columns[18][searchable]' : 'true',
'columns[18][orderable]' : 'true',
'columns[18][search][value]' : '',
'columns[18][search][regex]' : 'false',
'columns[19][data]' : 'wardsplacedPermin',
'columns[19][name]' : '',
'columns[19][searchable]' : 'true',
'columns[19][orderable]' : 'true',
'columns[19][search][value]' : '',
'columns[19][search][regex]' : 'false',
'columns[20][data]' : 'wardskilledPermin',
'columns[20][name]' : '',
'columns[20][searchable]' : 'true',
'columns[20][orderable]' : 'true',
'columns[20][search][value]' : '',
'columns[20][search][regex]' : 'false',
'order[0][column]' : 4,
'order[0][dir]' : 'desc',
'start' : 0,
'length' : 200,
'search[value]' : '',
'search[regex]' : 'false',
'area' : '',
'eid' : 956,
'type' : 'player',
'gametype' : 2,
'filter' : {"team":{},"player":{},"meta":{"4":"ADC"}}
}

# 自定义请求头信息，相关的头信息必须封装在字典结构中
headers = {
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
'content-length': '4920',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'cookie': 'wp_pvid=6866078069; UM_distinctid=172c723e149a4c-02bbc45b767c9d-31607403-13c680-172c723e14a560; gameType=2; wanplus_token=594af2125b0056d0e9138b9b93a5d535; wanplus_storage=lf4m67eka3o; wanplus_sid=bca0b60d1510938ad9b9db4616a15a67; wanplus_csrf=_csrf_tk_2020090033; wp_info=ssid=s9461324424; Hm_lvt_f69cb5ec253c6012b2aa449fb925c1c2=1594898724,1594898738,1594982969,1595159408; CNZZDATA1275078652=1521080111-1595242068-%7C1595247472; Hm_lpvt_f69cb5ec253c6012b2aa449fb925c1c2=1595251018',
'origin': 'https://m.wanplus.com',
'referer': 'https://m.wanplus.com/lol/playerstats',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'x-csrf-token': '2087198897',
'x-requested-with': 'XMLHttpRequest'
}

# 2.发起基于ajax的post请求
response = requests.post(url=url,data=data,headers=headers)

#获取响应内容：响应内容为json串
data = response.text
names = re.findall(r'"playername":"(.+?)",',data)
metas = re.findall(r'"meta":"(.+?)",',data)
golds = re.findall(r'"goldsPermin":"(.+?)",',data)
damage = re.findall(r'"damagetoheroPermin":"(.+?)",',data)
total_d = re.findall(r'"damagetohero":"(.+?)",',data)
death = re.findall(r'"deaths":"(.+?)",',data)
damage_trans = [int(damage[i])/int(golds[i]) for i in range(len(names))]
damage_per_death = [int(total_d[i])/int(death[i]) for i in range(len(damage))]

names_ADC = []
damage_trans_ADC = []
golds_ADC = []
damage_ADC = []
damage_per_death_ADC = []

for i in range(len(names)):
    if metas[i] == '\\u4e0a\\u5355':
        names_ADC.append(names[i])
        damage_trans_ADC.append(damage_trans[i])
        golds_ADC.append(golds[i])
        damage_ADC.append(int(damage[i]))
        damage_per_death_ADC.append(damage_per_death[i])

import matplotlib.pyplot as plt
colors = ['lightskyblue', 'deepskyblue', 'dodgerblue', 'royalblue', 'mediumblue', 'navy']
plt.rcParams['font.sans-serif']=['SimHei']

plt.xlabel('Damage conversion rate')
plt.ylabel('Damage per death')

for i in range(len(damage_trans_ADC)):
    plt.scatter(damage_trans_ADC[i], damage_per_death_ADC[i],color=random.choice(colors))
    plt.annotate(names_ADC[i], xy = (damage_trans_ADC[i], damage_per_death_ADC[i]), xytext = (damage_trans_ADC[i]+0.01, damage_per_death_ADC[i]+0.01)) # 这里xy是需要标记的坐标，xytext是对应的标签坐标
plt.show()
