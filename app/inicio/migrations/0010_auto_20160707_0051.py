# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 05:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inicio', '0009_auto_20160707_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorias', models.ManyToManyField(to='inicio.Categorias')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'docentes',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='rol',
            field=models.IntegerField(choices=[(1, 'Administrador'), (2, 'Docente'), (3, 'Acudiente')]),
        ),
    ]
