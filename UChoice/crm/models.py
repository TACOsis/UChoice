from django.db import models

# Create your models here.
class Order_Product(models.Model):
    Sur_Name = models.CharField(max_length=30, verbose_name="Фамилия")
    Firste_name = models.CharField(max_length=30, verbose_name="Имя")
    Last_name = models.CharField(max_length=30, verbose_name="Отчество")
    Adress = models.CharField(max_length=250, verbose_name="Адрес")
    Day = models.CharField(max_length=20, verbose_name="День желаемой доставки")
    Cridet_card = models.CharField(max_length=20, verbose_name="Кредитная карта")
    Product = models.CharField(max_length=20, verbose_name="Товар")

    def __str__(self):
        return self.Adress
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"