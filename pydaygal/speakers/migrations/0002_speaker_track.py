# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='track',
            field=models.IntegerField(default=0),
        ),
    ]
