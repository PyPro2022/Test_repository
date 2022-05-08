import requests

URL = 'https://bitpay.com/api/rates'
responce = requests.get(URL)
data = responce.json()

def get_currency(currency):
    global data
    for i in data:
        if currency.upper() in i.values():
            return i



def get_fields_names():
    global data
    fields_names = list(data[0].keys())
    return fields_names


def currency_info():
    global data
    for i in data:
        # print(f"code:{i['code']} | name: {i['name']}")

        return f"code:{i['code']} | name: {i['name']}"

'''
-----------------------------
TESTS
-----------------------------
'''


x= [{"code":"BTC","name":"Bitcoin","rate":1},{"code":"BCH","name":"Bitcoin Cash","rate":133.69},{"code":"USD","name":"US Dollar","rate":38507.54},{"code":"EUR","name":"Eurozone Euro","rate":36604.49}]

# y = get_currency('uah')
# z = currency_info()
# print(x[0].keys())
# print(y)

# print(list(data[0].keys()))