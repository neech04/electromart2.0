# Generated by Django 5.1.6 on 2025-03-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_order_product_remove_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product_name',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
