# Generated by Django 2.2.6 on 2021-04-22 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kafka', '0007_auto_20210421_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(name='topic', unique_together={('cluster_name', 'topic')},),
    ]
