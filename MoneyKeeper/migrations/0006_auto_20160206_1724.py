# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyKeeper', '0005_auto_20160206_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(),
        ),
    ]