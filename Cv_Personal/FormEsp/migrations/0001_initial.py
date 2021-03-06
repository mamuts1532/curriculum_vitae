# Generated by Django 3.1 on 2021-04-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormEspModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacion', models.CharField(max_length=50)),
                ('instituto', models.CharField(max_length=100)),
                ('mes_final', models.CharField(max_length=50)),
                ('ahno_final', models.PositiveIntegerField()),
                ('url_certificado', models.URLField()),
            ],
            options={
                'ordering': ['-ahno_final'],
            },
        ),
    ]
