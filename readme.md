# Binance Futures Testnet Trading Bot

A simple Python trading bot for Binance Futures Testnet (USDT-M).

This project can place:

- MARKET orders
- LIMIT orders

using Binance Futures Testnet API.

The project is made for learning purposes and uses Python CLI input with proper validation, logging, and error handling.

---

# Features

- Place BUY and SELL orders
- Support for MARKET and LIMIT order types
- Input validation
- Error handling
- Logging of API requests and responses
- Separate files for better code structure
- Uses Binance Futures Testnet (safe demo environment)

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Requirements

- Python 3.x
- Binance Futures Testnet account



# Install Dependencies

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

## Windows

```bash
.venv\Scripts\activate
```


Install required packages:

```bash
pip install -r requirements.txt
```



# Binance Testnet Setup

Open Binance Futures Testnet:

https://testnet.binancefuture.com

Create account and generate API keys from API Management.



# Environment Variables

Create a `.env` file in project folder:

```env
API_KEY=your_api_key
API_SECRET=your_secret_key
```



# Run MARKET Order

Example:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```



# Run LIMIT Order

Example:

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```


# Example Output

```text
Order Request Summary
---------------------
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.001

Order placed successfully!

Order Details:
Order ID: 12345678
Status: NEW
Executed Quantity: 0.001
```

---

# Logging

Logs are stored in:

```text
logs/trading_bot.log
```

The log file contains:
- API requests
- API responses
- Errors and exceptions

---

# Validation Added

The project validates:
- valid BUY/SELL side
- valid MARKET/LIMIT type
- quantity greater than 0
- LIMIT order must include price

---

# Assumptions

- User already has Binance Futures Testnet account
- User has test USDT balance in account
- Internet connection is available

---

# Important

This project uses Binance Futures Testnet only.

No real money is used.

---

# Future Improvements

Some features that can be added later:
- Stop-Limit orders
- Better CLI menu
- Simple UI
- Order history
