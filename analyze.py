# /bot/analyze.py

from utils import get_gmgn_trending, check_rug_score, get_twitter_sentiment

def analyze_market():
    trending = get_gmgn_trending()
    filtered = []

    for token in trending:
        safety = check_rug_score(token["address"])
        sentiment = get_twitter_sentiment(token["name"])

        if safety == "safe" and sentiment > 0.6:
            filtered.append(token)

    return filtered
