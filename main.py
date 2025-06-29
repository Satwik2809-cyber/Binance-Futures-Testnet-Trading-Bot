from trading_bot import BasicBot

api_key = input("🔑 Enter your Binance Testnet API Key: ")
api_secret = input("🔒 Enter your Binance Testnet API Secret: ")

bot = BasicBot(api_key, api_secret)

symbol = input("📈 Enter symbol (e.g., BTCUSDT): ")
side = input("🟢 BUY or 🔴 SELL: ")
order_type = input("📦 MARKET or LIMIT: ")
quantity = float(input("📊 Enter quantity: "))

price = None
if order_type.upper() == "LIMIT":
    price = float(input("💰 Enter limit price: "))

bot.place_order(symbol, side, order_type, quantity, price)
