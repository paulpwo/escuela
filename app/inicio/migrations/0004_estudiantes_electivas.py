# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_estudiantes_acudiente'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='electivas',
            field=models.ManyToManyField(related_name='eleconcate', to='inicio.Categorias'),
        ),
    ]