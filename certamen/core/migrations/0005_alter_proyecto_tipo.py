# Generated by Django 5.0.4 on 2024-06-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_proyecto_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='tipo',
            field=models.CharField(max_length=30, verbose_name='Tema Proyecto'),
        ),
    ]
