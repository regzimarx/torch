# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torch', '0002_auto_20171104_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='torch.Department'),
            preserve_default=False,
        ),
    ]