# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 20:08
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patreonmanager', '0002_fundraisingstatus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fundraisingstatus',
            options={'ordering': ('-date_updated',)},
        ),
    ]
