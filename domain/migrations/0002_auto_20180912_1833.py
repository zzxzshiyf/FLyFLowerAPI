# Generated by Django 2.1.1 on 2018-09-12 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 12, 18, 33, 15, 199316), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 12, 18, 33, 15, 200017), verbose_name='创建时间'),
        ),
    ]