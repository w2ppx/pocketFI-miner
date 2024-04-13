import requests
import time

raw_data = ['example', 'example1']

def get_headers(raw_data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6332.212 Safari/537.36',
        'telegramRawData': raw_data,
        'Referer': 'https://botui.pocketfi.org/',
        'Origin': 'https://botui.pocketfi.org',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }
    return headers

show = input('Show account id? (y/n): ')

session = requests.Session()

def mine():
    for data in raw_data:
        headers = get_headers(data)
        response = session.get('https://bot.pocketfi.org/mining/getUserMining', headers=headers)
        if response.status_code == 200:
            json_response = response.json()
            json = json_response["userMining"]
            print(f'{("[Account " + str(json["userId"]) + "]") if show == "y" else ""}Request sent. Balance: {json["gotAmount"]}/{json["miningAmount"]} SWITCH Current speed: {json["speed"]} switch/hour')
            if json["miningAmount"] >= 1.25:
                response = session.post('https://bot.pocketfi.org/mining/claimMining', headers=headers)
                if response.status_code == 200:
                    print(f'{("[Account " + str(json["userId"]) + "]") if show == "y" else ""}Claimed {json["miningAmount"]} SWITCH')
            return
        else:
            print('Error: PocketFI is down. Received status code:', response.status_code)
            return
        
while True:
    try:
        mine()
    except Exception as e:
        print('Error:', e)
    time.sleep(30)
    