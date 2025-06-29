# /bot/analyze.py

from utils import get_gmgn_trending, check_rug_score, get_twitter_sentiment

def analyze_market():
    token_address = "So11111111111111111111111111111111111111112"  # soon from GMGN or Twitter

    safety = check_token_safety(token_address)

    if safety is None or safety["honeypot"] or not safety["liquidity_locked"] or safety["score"] < 70:
        return None

    return token_address

