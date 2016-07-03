# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 20:45
from __future__ import unicode_literals

import json

from django.db import migrations
from django.utils.crypto import get_random_string

from callisto.delivery.models import _encrypt_report


def encrypt_match_report(apps, schema_editor):
    MatchReport = apps.get_model('delivery', 'MatchReport')
    for match_report in MatchReport.objects.all():
        match_report_text = {'identifier': match_report.identifier,
                             'perp_name': match_report.name,
                             'contact_name': match_report.contact_name,
                             'contact_email': match_report.contact_email,
                             'contact_phone': match_report.contact_phone,
                             'contact_voicemail': match_report.contact_voicemail,
                             'contact_notes': match_report.contact_notes}
        match_report.salt = get_random_string()
        encrypted_match_report = _encrypt_report(salt=match_report.salt, key=match_report.identifier,
                                                 report_text=json.dumps(match_report_text))
        match_report.encrypted = encrypted_match_report
        if match_report.seen:
            match_report.identifier = None
        match_report.save()


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_allow_deletion_of_identifier'),
    ]

    operations = [
         migrations.RunPython(encrypt_match_report, reverse_code=migrations.RunPython.noop),
    ]
