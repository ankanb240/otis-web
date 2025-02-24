# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-06 00:31
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0004_auto_20170806_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ta',
            name='user',
            field=models.ForeignKey(help_text='The Django Auth user attached to the TA', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
