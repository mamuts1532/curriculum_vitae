# Generated by Django 3.1 on 2021-04-21 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormAcad', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formacadmodel',
            options={'ordering': ['-fecha_final']},
        ),
    ]