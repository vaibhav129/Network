# Generated by Django 2.2.13 on 2020-10-10 20:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_auto_20201010_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilei',
            name='follower',
            field=models.ManyToManyField(blank=True, default=None, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
