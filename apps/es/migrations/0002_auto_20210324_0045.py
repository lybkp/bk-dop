# Generated by Django 2.2.6 on 2021-03-24 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(model_name='escluster', old_name='appid', new_name='app_id',),
    ]