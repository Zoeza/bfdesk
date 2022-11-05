# Generated by Django 4.1.1 on 2022-11-04 20:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('birthday', models.DateField(default=datetime.date(2022, 11, 4))),
                ('lawyer', models.CharField(max_length=100)),
            ],
        ),
    ]
