import random
import requests
import time
from fake_useragent import UserAgent

raw_data = [
    'example_1',
    'example_2'
]


ua_list = []

def generate_ua():
    for _ in range(len(raw_data)):
        ua = UserAgent(os='android').random
        ua_list.append(ua)

generate_ua()

def get_headers(raw_data, ua):
    headers = {
        'User-Agent': f'{ua}',
        'telegramRawData': raw_data,
        'Referer': 'https://pocketfi.app',
        'Origin': 'https://pocketfi.app',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }
    return headers

show = input('Show account id? (y/n): ')
# show = 'y'

session = requests.Session()

def mine():
    for index in range(len(raw_data)):
        time.sleep(random.randint(10, 25))
        headers = get_headers(raw_data[index], ua_list[index])
        response = session.get('https://rubot.pocketfi.org/mining/getUserMining', headers=headers)
        if response.status_code == 200:
            json_response = response.json()
            json = json_response["userMining"]
            print(f'{(str(index+1)+"[Account " + str(json["userId"]) + "] ") if show == "y" else ""}Request sent. Balance: {json["gotAmount"]}/{json["miningAmount"]} SWITCH Current speed: {json["speed"]} switch/hour')
            if json["miningAmount"] >= 0.2:
                response = session.post('https://rubot.pocketfi.org/mining/claimMining', headers=headers)
                if response.status_code == 200:
                    print(f'{("[Account " + str(json["userId"]) + "] ") if show == "y" else ""}Claimed {json["miningAmount"]} SWITCH')
            continue
        else:
            print('Error: PocketFI is down. Received status code:', response.status_code)


while True:
    try:
        mine()
        delay = random.randint(45, 65)*60
        print(f'⏳ Delay for {delay} seconds before next cycle')
        time.sleep(delay)
    except Exception as e:
        print('Error:', e)
