# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('course', models.CharField(choices=[(b'ELEM', b'Elementary Training Department'), (b'SHS', b'Senior High School'), (b'BSED', b'Bachelor in Secondary Education'), (b'BEED', b'Bachelor in Elementary Education'), (b'BSND', b'Bachelor of Science in Nutrition and Dietetics'), (b'BSM', b'Bachelor of Science in Midwifery'), (b'BSA', b'Bachelor of Science in Accountancy'), (b'BSAT', b'Bachelor of Science in Accounting Technology'), (b'BSOA', b'Bachelor of Science in Office Administration'), (b'BSIT', b'Bachelor of Science in Information Technology'), (b'BSCS', b'Bachelor of SCience in Computer Science'), (b'BLIS', b'Bachelor of Library Information Science'), (b'BSCE', b'Bachelor of Science in Computer Engineering'), (b'BSHRM', b'Bachelor of Science in Hotem and Restaurant Management'), (b'BSSW', b'Bachelor of Science in Social Work')], max_length=5)),
                ('department', models.CharField(max_length=5, null=True)),
                ('affiliations', models.TextField()),
                ('awards', models.TextField()),
            ],
        ),
    ]
