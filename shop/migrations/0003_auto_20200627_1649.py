# Generated by Django 3.0.7 on 2020-06-27 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200625_1052'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='Product',
        ),
    ]
