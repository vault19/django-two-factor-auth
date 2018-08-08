# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 04:50
from __future__ import unicode_literals

import django.db.models.deletion
import django_otp.util
from django.conf import settings
from django.db import migrations, models

import two_factor.models


class Migration(migrations.Migration):

    dependencies = [
        ('two_factor', '0004_auto_20160205_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonedevice',
            name='confirmed',
            field=models.BooleanField(default=True, help_text='Is this device ready for use?'),
        ),
        migrations.AlterField(
            model_name='phonedevice',
            name='key',
            field=models.CharField(default=django_otp.util.random_hex, help_text='Hex-encoded secret key', max_length=40),
        ),
        migrations.AlterField(
            model_name='phonedevice',
            name='method',
            field=models.CharField(choices=[('call', 'Phone Call'), ('sms', 'Text Message')], max_length=4, verbose_name='method'),
        ),
        migrations.AlterField(
            model_name='phonedevice',
            name='name',
            field=models.CharField(help_text='The human-readable name of this device.', max_length=64),
        ),
        migrations.AlterField(
            model_name='phonedevice',
            name='user',
            field=models.ForeignKey(help_text='The user that this device belongs to.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
