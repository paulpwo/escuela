# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_auto_20160621_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='acudiente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inicio.Profile'),
            preserve_default=False,
        ),
    ]
