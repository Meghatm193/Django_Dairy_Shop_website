# Generated by Django 4.2.2 on 2023-10-10 07:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_whishlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Whishlist',
            new_name='Wishlist',
        ),
    ]
