# Generated by Django 3.1.2 on 2020-10-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
