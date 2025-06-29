# /bot/utils.py

def get_gmgn_trending():
    # Simulated
    return [{"address": "TOKEN123", "name": "MEMECOIN"}]

def check_rug_score(token_address):
    # Simulated
    return "safe"

def get_twitter_sentiment(token_name):
    # Simulated
    return 0.7

def execute_trade(token_address, private_key):
    # Replace with Jupiter/Raydium trade
    return {
        "success": True,
        "price": 0.005,
        "timestamp": "2025-06-29T12:00:00Z"
    }

def should_sell(position):
    # Simulated logic (replace with real price check)
    return False
import requests

def check_token_safety(token_address):
    try:
        url = f"https://api.rugcheck.xyz/v1/tokens/{token_address}"
        response = requests.get(url)
        data = response.json()

        if not data.get("success", False):
            print("❌ RugCheck API failed.")
            return None

        result = data["data"]
        return {
            "honeypot": result.get("is_honeypot"),
            "liquidity_locked": result.get("liquidity_locked"),
            "owner_renounced": result.get("owner_renounced"),
            "score": result.get("score")
        }

    except Exception as e:
        print(f"⚠️ RugCheck error: {e}")
        return None
from utils import check_token_safety

def analyze_market():
    # Replace this with real token grabbing logic (from GMGN etc)
    token_address = "EXAMPLE_SOLANA_TOKEN"

    safety = check_token_safety(token_address)

    if safety is None:
        print("⚠️ Couldn’t get rugcheck data.")
        return None

    if safety["honeypot"]:
        print("❌ Token is a honeypot. Skipping.")
        return None

    if not safety["liquidity_locked"]:
        print("❌ Liquidity not locked. Skipping.")
        return None

    if safety["score"] < 70:  # up to you how strict
        print(f"❌ RugCheck score too low ({safety['score']}/100). Skipping.")
        return None

    print("✅ Passed RugCheck filters.")
    return token_address
