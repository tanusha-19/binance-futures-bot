# Binance Futures Trading Bot (Testnet)

## Setup
1. Clone the repository.
2. Install dependencies: `pip install python-binance python-dotenv`
3. Create a `.env` file and add your keys:
   - BINANCE_API_KEY=your_key
   - BINANCE_API_SECRET=your_secret

## How to Run
- **Market Order:** `python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001`
- **Limit Order:** `python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 95000`

## Assumptions
- Using Binance Futures Testnet (USDT-M).
- Price and Quantity must follow Binance's symbol filters (e.g., BTC precision).