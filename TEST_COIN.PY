from crypto_pay_api_sdk import cryptopay

Crypto = cryptopay.Crypto("73660:AA9mkuZVn1nWEBcQLKChXK8MPY4wZkTPt2R",testnet = False) #default testnet = False

# print(Crypto.getMe())
a= Crypto.createInvoice("TON", "1.0", params={"description": "Test Invoice",
                                                 "expires_in": 300
                                                 })
print(a['result'])
print(a['result']['status'])
# print(Crypto.transfer(2116070853,
#                 'TON',1.0, 
#                 'Z7uYXRl',params = {'comment': 'effe'}))
