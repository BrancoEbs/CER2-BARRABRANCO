# Generated by Django 5.0.4 on 2024-06-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_proyecto_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=25, verbose_name='Nombre Proyecto'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='profesor',
            field=models.CharField(default='Sin Seleccionar', max_length=25),
        ),
    ]
