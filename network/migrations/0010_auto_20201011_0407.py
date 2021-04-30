# Generated by Django 2.2.13 on 2020-10-10 22:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_profilei_follower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilei',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='profilei',
            name='following',
        ),
        migrations.AddField(
            model_name='post',
            name='follower',
            field=models.ManyToManyField(blank=True, default=None, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='following',
            field=models.ManyToManyField(blank=True, default=None, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
    ]