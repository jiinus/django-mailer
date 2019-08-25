# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-25 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0003_messagelog_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='dont_send_until',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='messagelog',
            name='message_id',
            field=models.TextField(db_index=True, editable=False, null=True),
        ),
    ]