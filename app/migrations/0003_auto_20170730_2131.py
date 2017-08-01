# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-30 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_client_document_printjob'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=256, null=True),
        ),
    ]