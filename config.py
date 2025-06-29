# /bot/config.py

PRIVATE_KEY = 7DfjL12cu4qdqFiyGgYLCwVFzHPgk85gGaEKH9SSL95m

TRADE_SETTINGS = {
    "profit_target_pct": 50,
    "stop_loss_pct": 20,
    "max_open_trades": 4,
    "wallet_spend_ratio": 0.1  # 10% per trade
}

API_KEYS = {
    "gmgn": <https://gmgn.ai/defi/router/v1/sol/tx/get_swap_route?token_in_address=${inputToken}&token_out_address=${outputToken}&in_amount=${amount}&from_address=${fromAddress}&slippage=${slippage}>
    "rugcheck": "YOUR_RUGCHECK_API_KEY"
}

WATCHLIST_ADDRESSES = [
    "suqh5sHtr8HyJ7q8scBimULPkPpA557prMG47xCHQfK"  # Cupsey's wallet
]
