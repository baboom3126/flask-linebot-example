from flask import Flask, request, abort,render_template
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('rhYY7ZIgUXtkD042bs3shMfLlmliLCsUdUC3RzhQMFyG0MU1zv++Cu3hD3JBsBKFmArlnxiQujc4RRIadecPGDQG3gP1dwqSkGl3SH7Sg+zmnhNISryz6h7ArFp7FVEL1ZLLOfsTZaYz6EXLkeWa+wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('22512e0d32729d5734a80db99b44729c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/test')
def homes():
  return """123"""

if __name__ == "__main__":
    app.run()
