# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20181009_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_html',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
    ]
