# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 22:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'Grupo'), (2, 'Electiva')])),
                ('categoria', models.CharField(max_length=144)),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=144)),
                ('contenido', models.TextField()),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.Categorias')),
            ],
            options={
                'db_table': 'contenido',
            },
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.CharField(max_length=144)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.Categorias')),
            ],
            options={
                'db_table': 'estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('contenido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.Contenido')),
            ],
            options={
                'db_table': 'galeria',
            },
        ),
        migrations.CreateModel(
            name='Institucional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colegio', models.CharField(max_length=144)),
                ('direccion', models.CharField(max_length=144)),
                ('telefono', models.IntegerField()),
                ('ciudad', models.CharField(max_length=144)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(max_length=144)),
                ('twitter', models.CharField(max_length=144)),
            ],
            options={
                'db_table': 'institucional',
            },
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechayhora', models.DateTimeField(auto_now=True)),
                ('contenido', models.TextField()),
            ],
            options={
                'db_table': 'notificaciones',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.IntegerField(choices=[(1, '')])),
                ('cedula', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=144)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
