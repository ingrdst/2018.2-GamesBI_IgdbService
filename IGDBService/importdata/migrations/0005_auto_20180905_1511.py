# Generated by Django 2.1.1 on 2018-09-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importdata', '0004_auto_20180904_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='igdbgame',
            name='genres',
            field=models.ManyToManyField(to='importdata.Genre'),
        ),
    ]
