from django.db import models

# Create your models here.
class OrderBot(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name="Token")
    chat_id = models.CharField(max_length=200, verbose_name="chat_id")
    message = models.TextField(verbose_name="text")

    def __str__(self):
        return self.chat_id
    
    class Meta:
        verbose_name = "Настройку"
        verbose_name_plural = "Настройки"