from binance.client import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.basicConfig(filename='trading_bot.log', level=logging.INFO)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity
            }

            if order_type.upper() == 'LIMIT':
                params['price'] = price
                params['timeInForce'] = 'GTC'

            response = self.client.futures_create_order(**params)
            logging.info(f"Order Placed: {response}")
            print(f"✅ Order executed: {response['status']} | Order ID: {response['orderId']}")
        except Exception as e:
            logging.error(f"Error placing order: {e}")
            print(f"❌ Error: {e}")
