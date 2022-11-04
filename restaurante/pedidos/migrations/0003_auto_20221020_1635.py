# Generated by Django 3.2.15 on 2022-10-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20221012_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informacion',
            options={'verbose_name': 'Información', 'verbose_name_plural': 'Información'},
        ),
        migrations.AlterModelOptions(
            name='mesa',
            options={'verbose_name': 'Mesas', 'verbose_name_plural': 'Mesas'},
        ),
        migrations.AddField(
            model_name='mesa',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]