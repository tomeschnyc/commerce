# Generated by Django 3.1.3 on 2020-11-20 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20201120_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
