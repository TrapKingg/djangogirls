# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-06 19:31
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_move_event_page_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date',), 'verbose_name_plural': 'List of events'},
        ),
    ]
