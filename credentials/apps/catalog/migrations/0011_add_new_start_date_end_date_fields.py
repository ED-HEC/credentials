# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-31 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20180828_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='end_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='courserun',
            name='start_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
