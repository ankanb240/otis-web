# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_mockolympiad_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='start_date',
            field=models.DateField(blank=True, help_text='When the assignment opens. Leave blank if not active this semester.', null=True),
        ),
    ]