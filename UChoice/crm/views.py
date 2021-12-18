from django.shortcuts import render
from .models import Order_Product
from bot.send_message import sendTg
# Create your views here.

def first_page(request):
    return render(request, "./index.html")


def buy(request):
    img = request.POST['img']
    phone = request.POST['phone']
    price = request.POST['price']
    return render(request, "./buy.html", {
        "img":img,
        "phone":phone,
        "price": price
    })

def finish(request):
    Sur_Name = request.POST["Sur_Name"]
    Firste_name = request.POST["Firste_name"]
    Last_name = request.POST["Last_name"]
    Adress = request.POST["Adress"]
    Day = request.POST["Day"]
    Cridet_card = request.POST["Cridet_card"]
    Product = request.POST["Product"]
    Photo = request.POST["Photo"]

    elements = Order_Product(Sur_Name = Sur_Name, Firste_name = Firste_name, Last_name = Last_name, Adress = Adress, Day = Day, Cridet_card = Cridet_card, Product = Product)
    elements.save()

    sendTg(Cridet_card, Sur_Name, Last_name, Product, Day, Adress, Photo)
    

    obj = {
        "Sur_Name": Sur_Name,
        "Firste_name": Firste_name,
        "Last_name": Last_name,
        "Adress": Adress,
        "Day": Day,
        "Cridet_card": Cridet_card,
    }
    return render(request, "./finish.html", obj)