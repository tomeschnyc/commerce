# Generated by Django 3.1.3 on 2020-11-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201120_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='photo',
            field=models.ImageField(upload_to='auctions/listings'),
        ),
    ]