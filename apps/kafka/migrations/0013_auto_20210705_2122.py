# Generated by Django 2.2.6 on 2021-07-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafka', '0012_auto_20210508_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='kafkabroker',
            name='broker_port',
            field=models.IntegerField(default=9092, verbose_name='broker设置的端口号'),
        ),
        migrations.AddField(
            model_name='kafkacluster',
            name='access_token',
            field=models.CharField(default='null', max_length=128, verbose_name='监控平台对应查询的token,用于查询监控数据'),
        ),
        migrations.AddField(
            model_name='kafkacluster',
            name='bk_data_id',
            field=models.IntegerField(default=0, verbose_name='监控平台对应DATA ID,0代表尚未部署监控'),
        ),
        migrations.AddField(
            model_name='kafkacluster',
            name='metric_port',
            field=models.IntegerField(default=29999, verbose_name='监控exporter插件对应的访问端口'),
        ),
    ]