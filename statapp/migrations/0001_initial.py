# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('path', models.CharField(max_length=15)),
            ],
        ),
    ]
