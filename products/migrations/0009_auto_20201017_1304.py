# Generated by Django 3.1.2 on 2020-10-17 13:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_auto_20201017_1257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductReviews',
            new_name='ProductReview',
        ),
    ]