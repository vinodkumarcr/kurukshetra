# Generated by Django 2.1.2 on 2018-10-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandesh', '0002_auto_20181022_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
