# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-15 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='group',
        ),
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
    ]