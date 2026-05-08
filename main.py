import argparse
import logging
from bot.client import BinanceBot

# 1. Setup Logging to a file (Required by the task!)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("bot_activity.log"), # This creates the log file
        logging.StreamHandler()                # This prints to your screen
    ]
)

def main():
    # 2. Setup the CLI Arguments
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price (Required for LIMIT orders)")

    args = parser.parse_args()

    # 3. Initialize Bot and Place Order
    bot = BinanceBot()
    result = bot.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.qty,
        price=args.price
    )

    # 4. Print Summary
    if "orderId" in result:
        print("\n✅ ORDER PLACED SUCCESSFULLY")
        print(f"Order ID: {result['orderId']}")
        print(f"Status: {result['status']}")
        print(f"Quantity: {result['origQty']}")
    else:
        print(f"\n❌ ORDER FAILED: {result.get('error')}")

if __name__ == "__main__":
    main()