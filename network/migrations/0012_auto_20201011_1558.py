# Generated by Django 2.2.13 on 2020-10-11 10:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_auto_20201011_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilei',
            name='follower',
            field=models.ManyToManyField(blank=True, default=None, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profilei',
            name='following',
            field=models.ManyToManyField(blank=True, default=None, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
    ]
