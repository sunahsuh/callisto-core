# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_delete_encrypted_fields_from_match_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='autosaved',
            field=models.BooleanField(default=False, null=False),
        ),
    ]
