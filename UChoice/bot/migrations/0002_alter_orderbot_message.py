# Generated by Django 3.2.7 on 2021-10-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbot',
            name='message',
            field=models.TextField(verbose_name='text'),
        ),
    ]
