# /bot/main.py

import time
from trade_engine import execute_strategy
from analyze import analyze_market

def run_bot():
    while True:
        print("[📊] Analyzing market...")
        market_data = analyze_market()

        print("[⚡] Executing strategy...")
        execute_strategy(market_data)

        print("[🕒] Sleeping for 60 minutes...\n")
        time.sleep(3600)

if __name__ == "__main__":
    run_bot()
