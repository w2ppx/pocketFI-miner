# pocketFI-miner

PocketFI miner with multiple accounts support

## Installation

To install the pocketFI-miner, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/w2ppx/pocketFI-miner.git
   ```
2. Install dependencies (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```
3. Extract raw data from tgweb:
   1. Open [Telegram Web](https://web.telegram.org/a/#6546647202)
   2. Open DevTools and open web app
   3. Find "telegramRawData" in any request to bot.pocketfi.org
   4. Fill it in the dictionary. You can also add multiple raw datas to mine from all accounts.
4. Run the script!
   ```bash
   python3 main.py
   ```

## Issues

If you have any problems with the script, you can send it to Issues tab, i'll be sure to help you.
