# Generated by Django 2.1 on 2018-08-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pineapple', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('internal_id', models.BigIntegerField(blank=True, db_column='Внутренний ID', null=True)),
                ('time_of_order_creation', models.TextField(blank=True, db_column='Время создания заказа', null=True)),
                ('merchant_id', models.BigIntegerField(blank=True, db_column='ID мерчанта', null=True)),
                ('status', models.TextField(blank=True, db_column='Статус', null=True)),
                ('sum', models.TextField(blank=True, db_column='Сумма', null=True)),
                ('currency', models.TextField(blank=True, db_column='Валюта', null=True)),
                ('order_id', models.TextField(blank=True, db_column='ID заказа', null=True)),
                ('order_type', models.TextField(blank=True, db_column='Тип заказа', null=True)),
                ('order_description', models.TextField(blank=True, db_column='Описание заказа', null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Test',
            new_name='PineappleTest',
        ),
    ]
