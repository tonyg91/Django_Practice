# Generated by Django 4.0 on 2021-12-16 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_supply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('paperweight', models.CharField(max_length=100)),
                ('sizes', models.CharField(max_length=100)),
                ('pages', models.IntegerField(default=3)),
            ],
        ),
    ]
