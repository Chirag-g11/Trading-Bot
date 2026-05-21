from bot.client import client
from bot.logging_config import logger
from binance.exceptions import BinanceAPIException

def place_order(symbol, side, order_type, quantity, price=None):

    try:
        logger.info(
            f"Request -> Symbol:{symbol}, Side:{side}, "
            f"Type:{order_type}, Qty:{quantity}, Price:{price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(f"Response -> {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise