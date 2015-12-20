# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='chosen',
            field=models.BooleanField(default=False, verbose_name='escolhido'),
        ),
        migrations.AddField(
            model_name='member',
            name='raffled',
            field=models.BooleanField(default=False, verbose_name='sorteou'),
        ),
    ]