# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bautizado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_Bautizado', models.CharField(max_length=500)),
                ('Apellidos_Bautizado', models.CharField(max_length=500)),
                ('Id_Reg_Civil', models.CharField(unique=True, max_length=15)),
                ('Fecha_Nacimiento', models.DateField()),
                ('Lugar_Nacimiento', models.CharField(max_length=255)),
                ('Telefono', models.CharField(max_length=7)),
                ('Celular', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=500)),
                ('Registro_civil', models.ImageField(upload_to=b'Registro_Civil')),
                ('Nombre_Padrino', models.CharField(max_length=500, blank=True)),
                ('Apellidos_Padrino', models.CharField(max_length=500, blank=True)),
                ('Cedula_Padrino', models.CharField(unique=True, max_length=20, blank=True)),
                ('Estado_Civil_Padrino', models.CharField(default=b'2', max_length=1, blank=True, choices=[(b'1', b'Casado'), (b'2', b'Soltero'), (b'3', b'Viudo')])),
                ('Email_Padrino', models.EmailField(max_length=254, blank=True)),
                ('Fotocopia_Cedula_Padrino', models.ImageField(upload_to=b'Fot_Celula_Padrino', blank=True)),
                ('Nombre_Madrina', models.CharField(max_length=500, blank=True)),
                ('Apellidos_Madrina', models.CharField(max_length=500, blank=True)),
                ('Cedula_Madrina', models.PositiveIntegerField(unique=True, null=True, blank=True)),
                ('Estado_Civil_Madrina', models.CharField(default=b'2', max_length=1, blank=True, choices=[(b'1', b'Casado'), (b'2', b'Soltero'), (b'3', b'Viudo')])),
                ('Email_Madrina', models.EmailField(max_length=254, blank=True)),
                ('Fotocopia_Cedula_Madrina', models.ImageField(upload_to=b'Fot_Celula_Madrina', blank=True)),
                ('Aprobado', models.NullBooleanField()),
                ('ya_Bautizado', models.NullBooleanField()),
                ('Fecha_del_Bautizo', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='padres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_Padre', models.CharField(max_length=250)),
                ('Apellidos_Padre', models.CharField(max_length=250)),
                ('Cedula_Padre', models.CharField(unique=True, max_length=20)),
                ('Email_Padre', models.EmailField(unique=True, max_length=254)),
                ('Nombre_Abuelo_Paterno', models.CharField(max_length=500)),
                ('Nombre_Abuela_Paterna', models.CharField(max_length=500)),
                ('Nombre_Madre', models.CharField(max_length=500)),
                ('Apellidos_Madre', models.CharField(max_length=500)),
                ('Cedula_Madre', models.CharField(unique=True, max_length=20)),
                ('Email_Madre', models.EmailField(unique=True, max_length=254)),
                ('Nombre_Abuelo_Materno', models.CharField(max_length=500)),
                ('Nombre_Abuela_Materna', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='bautizado',
            name='Padres',
            field=models.ForeignKey(to='prebautismal.padres'),
        ),
    ]
