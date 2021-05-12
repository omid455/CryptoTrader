# CryptoTrader
Utilities to help monitor market and get vital information using cex.io API and pyhton using [www.cex.io](https://cex.io/r/1/up118720912/1) exchange, a trusted and simple to use crypto market.

### Libraries needed (some builtin, some installed via pip):

cexio (pip install cexio)

time

datetime

os 

json

### Credentials:
You need to put your own username and password and api key in the creds.json file.

### market_intel.py
Shows live prices for the selected cryptos (you can add or remove from the list inside the file), shows your available cash and on orders, shows your crypto holdings and finally your orders. 
Note: if you change the number of coins in the list, you should change the while loop number accordignly, currently 17.

**Disclaimer: These utilities were created for my own personal use as tools to monitor the market and make decisions for trading crypto. shared here to help people have an easier access to information.use at your own risk. no guarantees.**
