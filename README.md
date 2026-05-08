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
