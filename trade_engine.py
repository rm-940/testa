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
