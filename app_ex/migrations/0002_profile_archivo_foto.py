# Generated by Django 3.1.5 on 2021-01-23 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='archivo_foto',
            field=models.CharField(default='sin asignar', max_length=400),
        ),
    ]
