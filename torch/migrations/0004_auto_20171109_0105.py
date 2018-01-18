# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torch', '0003_studentrecord_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='address',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentrecord',
            name='birthday',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentrecord',
            name='eligibility',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentrecord',
            name='scholarships',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]