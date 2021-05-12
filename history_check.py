import cexio
import json

creds = json.load(open("creds.json", "r"))
api = cexio.Api(creds["username"], creds["api_key"], creds["api_secret"])

coin = input("Please enter the coin name to check order history: ")
hist = api.archived_orders(coin.upper()+"/USD", status='d')
hist_number = len(hist)
print("You can enter a maximum of ", hist_number)
trans = int(input("Please enter the number of transactions to show: "))

index = 0
while index < trans:
    hist = api.archived_orders(coin.upper()+"/USD", status='d')
    price = api.last_price(market=coin.upper()+'/USD')
    key_check = hist[index]
    search_key = "price"
    if search_key in key_check:
        last_transaction_price = round(float(hist[index]["price"]), 4)
        last_coin = price['curr1']
        last_transaction_type = hist[index]['type']
        t_date = hist[index]['time']
        t_date = t_date[:10]
        crypto_amount = round(float(hist[index]['amount']), 2)
        usd_amount = hist[index]["a:USD:cds"]
        index = index + 1
        print(index, "Date:", t_date, last_coin, "  price: ", last_transaction_price, "     amount: ", crypto_amount, "     USD amount: ", usd_amount, "    type: " , last_transaction_type)
    else:
        index = index + 1
        print("Transaction", index, "ignored because there is no price.")



