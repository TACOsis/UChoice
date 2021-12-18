import requests

token = "2042097971:AAFMjRdlh4HKkmy0_wPYh-5nhfca26GlBnQ"
chat_id = "717429263"
text = "Test_1"

def Aboba():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    requests.post(method, data= {
        "chat_id": chat_id,
        "text": text
    })


Aboba()