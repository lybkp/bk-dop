# Generated by Django 2.2.6 on 2021-05-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0008_auto_20210421_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escluster',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='escluster',
            name='colds',
        ),
        migrations.RemoveField(
            model_name='escluster',
            name='datas',
        ),
        migrations.RemoveField(
            model_name='escluster',
            name='masters',
        ),
        migrations.RemoveField(
            model_name='esnodeinfo',
            name='app',
        ),
        migrations.RemoveField(
            model_name='esrule',
            name='appid',
        ),
        migrations.AddField(
            model_name='escluster',
            name='client_cnt',
            field=models.IntegerField(default=0, verbose_name='协调节点数量'),
        ),
        migrations.AddField(
            model_name='escluster',
            name='cold_cnt',
            field=models.IntegerField(default=0, verbose_name='冷节点数量'),
        ),
        migrations.AddField(
            model_name='escluster',
            name='data_cnt',
            field=models.IntegerField(default=0, verbose_name='数据节点数量'),
        ),
        migrations.AddField(
            model_name='escluster',
            name='master_cnt',
            field=models.IntegerField(default=0, verbose_name='master数量'),
        ),
        migrations.AddField(
            model_name='esnodeinfo',
            name='app_id',
            field=models.IntegerField(default=0, verbose_name='业务id'),
        ),
        migrations.AddField(
            model_name='esrule',
            name='app_id',
            field=models.IntegerField(default=0, verbose_name='业务id'),
        ),
        migrations.AlterField(
            model_name='escluster',
            name='app_id',
            field=models.IntegerField(default=0, verbose_name='业务id'),
        ),
    ]
