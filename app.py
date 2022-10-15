import telebot
from flask import Flask, request
from binance.client import Client
from binance.enums import *
import json, config


app = Flask(__name__)


client = Client(config.api_key, config.api_secret)

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"sending order {order_type} - {side} {quantity} {symbol}")
        order = client.create_order(
            symbol=symbol, side=side, type=order_type, quantity=quantity
        )
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return order


@app.route("/webhook", methods=["POST"])
def webhook():

    data = json.loads(request.data)
    side = data["startegy"]["order_action"].upper()
    quantity = data["startegy"]["order_contracts"]
    ticker = data["ticker"]

    telebot.TeleBot(config.telegramBotApi).send_message(
        config.telegramUserId,
        f"""{data["time"]}
                                                                         {data["exchange"]}:{data["ticker"]}
                                                                         FİYAT = {data}
                                                                         ALARM TİPİ = {data["strategy"]["order_price"]}
                                                                        """,
    )

    order_response = order(side, quantity, ticker)
    print(order_response)

    if order_response:
        return {
                "code": "success"
                }
    else:
        print("order failed")
        return {
                "code": "error", 
                "message": "order failed "
                }


if __name__ == "__main__":
    app.run()
