# Generated by Django 2.1.1 on 2018-09-12 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0002_auto_20180912_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='ctime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='ctime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]