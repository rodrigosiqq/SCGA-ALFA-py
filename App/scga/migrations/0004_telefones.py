# Generated by Django 4.1.4 on 2022-12-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scga', '0003_rename_serial_impressoras_cupsid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefones',
            fields=[
                ('identel', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=12)),
                ('ramal', models.CharField(max_length=20)),
                ('setor', models.CharField(max_length=10)),
            ],
        ),
    ]
