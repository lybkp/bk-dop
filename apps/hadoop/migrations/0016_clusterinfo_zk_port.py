# Generated by Django 2.2.6 on 2021-05-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop', '0015_clusterdetail_app_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='clusterinfo',
            name='zk_port',
            field=models.IntegerField(default=2181, verbose_name='zookeeper访问端口'),
        ),
    ]
