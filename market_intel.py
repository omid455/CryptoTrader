import cexio
import time
import datetime
from os import system
import json
from pandas_datareader import data as wb

creds = json.load(open("creds.json", "r"))
api = cexio.Api(creds["username"], creds["api_key"], creds["api_secret"])
dt = datetime.date.today()

def main():

# NOTE: Live Prices section:

    coin_list = ["BTC", "ETH", "ADA", "UNI", "LINK", "ATOM", "DOT", "MHC", "OMG", "ONG", "XRP", "ZRX", "TRX", "BAT",
                 "LTC", "BCH", "HOT"]
    name_list = []
    price_list = []
    low_list = []
    high_list = []
    change_list = []
    for coin in coin_list:
        ticker = api.ticker(coin + "/USD")
        coin_price = float(ticker["last"])
        low = float(ticker["low"])
        high = float(ticker["high"])
        percent = (low / high) * 100
        result_available = round(100 - percent, 2)
        name_list.append(coin)
        price_list.append(coin_price)
        low_list.append(low)
        high_list.append(high)
        change_list.append(result_available)


    index = 0
    output = list()
    output.append("Live Market Price:")

    while index < 17:
        prices_list = name_list[index], price_list[index], "Low:", low_list[index], "High:", high_list[index], "C:",change_list[index]
        output.append(prices_list)
        index = index + 1
    output.append("\n")

# NOTE: Assets section:

    balance = api.balance
    balance.pop("timestamp")
    balance.pop("username")

    usd_balance_available = "$ Available: ", balance["USD"]["available"]
    usd_balance_orders = "$ Orders: ", balance["USD"]["orders"]
    output.append("Cash:")
    output.append(usd_balance_available)
    output.append(usd_balance_orders)
    output.append("\n")

    balance.pop("USD")
    output.append("Crypto Assets:")


    for i in balance:
        result_available = float(balance[i]["available"])
        result_on_order = float(balance[i]["orders"])

        if result_available > 0.05:
            price = api.last_price(i + "/USD")["lprice"]
            price = float(price)
            assets = i, round(result_available, 2), "Equals to:", round(result_available * price, 2), "in USD!", "\n"
            output.append(assets)
        elif result_on_order > 0.05:
            price = api.last_price(i + "/USD")["lprice"]
            price = float(price)
            assets = i, round(result_on_order, 2), "Equals to:", round(result_on_order * price, 2), "in USD!", "\n"
            output.append(assets)
        else:
            pass

# NOTE: Show orders section:
    output.append("Orders:")

    orders = api.open_orders(market="")
    number_of_orders = len(orders)

    if orders:
        index = 0
        while index < number_of_orders:
            orders_list = orders[index]["symbol1"], orders[index]["type"], "price:", orders[index]["price"], "amount:", round(float(orders[index]["amount"])), "$"+str(round(float(orders[index]["amount"])*float(orders[index]["price"]))), "pending:", round(float(orders[index]["pending"])), "\n"
            output.append(orders_list)
            index = index + 1


# NOTE: TL price section:
    output.append("FX rates:")

    try:
        tl = wb.DataReader('USDTRY=X', data_source='yahoo', start=dt)['Close']
        tl = round(tl[0], 3)


        tl_price = "USD/TRY      ", "Base: 8.39      ", "l_price: ", tl
        output.append(tl_price)
    except:
        output.append("Market closed today for FX")

# NOTE: Print and rerun section:

    system("clear")

    for i in output:

        print(*i, sep=" ")


    time.sleep(60)
    main()


if __name__ == '__main__':
    main()