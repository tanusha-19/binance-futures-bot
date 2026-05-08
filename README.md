# Binance Futures Trading Bot (Testnet)

A robust, modular Python application designed to interact with the Binance Futures USDT-M Testnet. This bot allows users to execute trades via a Command Line Interface (CLI) while maintaining structured logs for all activity.

---

## 🛠 Project Structure
The project follows a modular design to separate API communication from execution logic:
- `main.py`: The entry point (CLI layer) that handles user input.
- `bot/client.py`: The core API layer that communicates with Binance.
- `bot/__init__.py`: Makes the bot directory a Python package.
- `bot_activity.log`: Contains historical records of all executed orders.

---

## 🚀 Setup Steps

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/tanusha-19/binance-futures-bot.git](https://github.com/tanusha-19/binance-futures-bot.git)
   cd binance-futures-bot
   ```

2. **Install Requirements:**
   Ensure you have Python 3.11+ installed. Install the necessary libraries:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
Create a .env file in the root directory and add your Binance Testnet API credentials:
```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```
---

## 📈 How to Run (Examples)
The bot uses argparse to handle commands. Use the following formats:

1. **Place a MARKET Order**
Executes immediately at the current market price.
```
python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

2. **Place a LIMIT Order**
Places an order on the book to execute at a specific price.
```
python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 95000
```

## 📝 Deliverables & Logs
This repository includes:

1. Source Code: Modularized for scalability.

2. requirements.txt: All necessary libraries (python-binance, python-dotenv).

3. bot_activity.log: Contains the results of the required test runs:

     - One MARKET order execution.

     - One LIMIT order execution.
  


