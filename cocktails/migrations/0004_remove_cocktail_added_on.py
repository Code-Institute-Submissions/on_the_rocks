# Generated by Django 3.1.2 on 2020-10-29 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0003_cocktail_product_measure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='added_on',
        ),
    ]
