# Generated by Django 5.0.7 on 2024-08-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEstudio', models.CharField(max_length=50)),
                ('duracion', models.CharField(max_length=50)),
                ('instituto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puestoTrabajo', models.CharField(max_length=50)),
                ('duracion', models.CharField(max_length=50)),
                ('nombreLugar', models.CharField(max_length=50)),
                ('locacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, null=True)),
                ('idioma', models.CharField(max_length=50, null=True)),
                ('nivelIdioma', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
