# /bot/trade_engine.py

from config import TRADE_SETTINGS, PRIVATE_KEY
from utils import execute_trade, should_sell

open_positions = []

def execute_strategy(market_data):
    for token in market_data:
        if len(open_positions) >= TRADE_SETTINGS["max_open_trades"]:
            break

        result = execute_trade(token["address"], PRIVATE_KEY)

        if result["success"]:
            open_positions.append({
                "token": token["address"],
                "buy_price": result["price"],
                "timestamp": result["timestamp"]
            })

    for position in open_positions[:]:
        if should_sell(position):
            # Sell logic here
            open_positions.remove(position)

def execute_strategy(token_address):
    print(f"🚀 Ready to snipe token: {token_address}")
    # insert buy logic here (e.g. via Jupiter)

import requests

def execute_strategy(token_address):
    print(f"🧠 Simulating buy for token: {token_address}")

    # Example Jupiter quote URL for USDC → token
    url = f"https://quote-api.jup.ag/v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint={token_address}&amount=10000000&slippage=1"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("✅ Jupiter Quote Found:")
        print(data)
    else:
        print("❌ Jupiter API failed")

