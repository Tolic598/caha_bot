from cryptomus import Client

PAYMENT_KEY = 'peEJqFN7i8NRB8C9qguLJgyD7vcYPsbKXpS2r2mpvlVHaDdwv1NWTxTFysH2Oy8gcoJztVViNeNK3G1oBcuBTllCr7Fw7l3qBATtKtHbZgzO5hgaNAmFpxYaUbzNEBf9'
MERCHANT_UUID = '37dbfdfd-3164-40e0-b072-ee4aa988f2af'

payment = Client.payment(PAYMENT_KEY, MERCHANT_UUID)
payout = Client.payout(PAYMENT_KEY, MERCHANT_UUID)

# balance = payment.balance()
# print(balance)

data = {
    'network': 'TRON',
    'currency': 'TRX',
    'order_id': '1',
}

result = payment.create_wallet(data)
print(result['address'])

page = 1
result1 = payment.history(page)
print(result1)
print(result1['items'][1]['uuid'])
# print(result1['items'][0]['amount'].replace(".00000000" , ""))

# data = {
#     "amount": "1",
#     "currency": "USDT", 
#     "network": "TRON", 
#     "order_id": "1",
#     "address": "TNr1U4DkWhR56B5sPh5AVBqszdtu4vyFrY",
#     "is_subtract": "1",
# }

# result2 = payout.create(data)
# print(result2)

