# Generated by Django 5.1.6 on 2025-03-24 07:45

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=5),
        ),
    ]
