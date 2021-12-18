import requests
from .models import OrderBot

def sendTg(Cridet_card, Sur_Name, Last_name, Product, Day, Adress, Photo):
    settings = OrderBot.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.chat_id)
    Photo = str(Photo.replace('.png', ''))
    Photo = str(Photo.replace('.jfif', ''))
    Photo_new = str(Photo.replace('/static/img/', ''))
    url = ''
    
    if (Photo_new == "iphone-13-pro"):
        url = "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/" + Photo_new + "-family-hero?wid=470&hei=556&fmt=png-alpha&.v=1631220221000"
    elif (Photo_new == "iphone-13"):
        url = "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/" + Photo_new + "-family-select-2021?wid=470&hei=556&fmt=jpeg&qlt=95&.v=1629842667000"
    elif (Photo_new == "iphone-12"): 
        url = "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/" + Photo_new + "-family-select-2021?wid=470&hei=556&fmt=jpeg&qlt=95&.v=1617135051000"
    elif (Photo_new == "iphone11"): 
        url = "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/" + Photo_new + "-select-2019-family?wid=441&hei=529&fmt=jpeg&qlt=95&.v=1567022175704"
    elif (Photo_new == "iphone-se"): 
        url = "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/" + Photo_new + "-family-select-2020?wid=441&hei=529&fmt=jpeg&qlt=95&.v=1586794486444"
    else:
        url = "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/" + Photo_new + "-hero-select-202011?wid=470&hei=556&fmt=jpeg&qlt=95&.v=1604709293000"

    message = url + "&caption=" + "Имя: " + Sur_Name + "\n" + "\n" + "Отчество: " + Last_name + "\n" + "\n" + "Телефон: " + Cridet_card  + "\n" + "\n" + "Продукт: " + Product + "\n" + "\n" + "Желаемый день доставки: " + Day + "\n" + "\n" + "Адрес доставки: " + Adress
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendPhoto?' + "chat_id=" + chat_id + "&" + "photo=" + message

    requests.post(method, data= {
        "chat_id": chat_id,
        "message": message
    })