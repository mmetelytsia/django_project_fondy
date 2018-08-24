# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Orders(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    internal_id = models.BigIntegerField(db_column='Внутренний ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_of_order_creation = models.TextField(db_column='Время создания заказа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    merchant_id = models.BigIntegerField(db_column='ID мерчанта', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Статус', blank=True, null=True)  # Field name made lowercase.
    sum = models.TextField(db_column='Сумма', blank=True, null=True)  # Field name made lowercase.
    currency = models.TextField(db_column='Валюта', blank=True, null=True)  # Field name made lowercase.
    order_id = models.TextField(db_column='ID заказа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_type = models.TextField(db_column='Тип заказа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_description = models.TextField(db_column='Описание заказа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return str(self.internal_id)

class PineappleTest(models.Model):
    test_field = models.CharField(max_length=200)
