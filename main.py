from trade_engine import execute_strategy
from analyze import analyze_market

def run_bot():
    while True:
        print("📈 Analyzing market...")
        token = analyze_market()

        if token:
            print(f"✅ Token passed analysis: {token}")
            execute_strategy(token)
        else:
            print("❌ No good tokens found. Waiting...")

        time.sleep(3600)  # or less for faster testing
