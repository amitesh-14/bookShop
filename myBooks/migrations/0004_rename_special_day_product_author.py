# Generated by Django 3.2.23 on 2024-02-01 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBooks', '0003_product_special_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='special_day',
            new_name='author',
        ),
    ]