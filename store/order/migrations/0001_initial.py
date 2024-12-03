# Generated by Django 5.0.4 on 2024-04-08 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_address', models.CharField(default='', max_length=255)),
                ('order_description', models.TextField(default='')),
                ('status', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
            ],
        ),
    ]