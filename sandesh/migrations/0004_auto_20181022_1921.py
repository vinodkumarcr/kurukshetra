# Generated by Django 2.1.2 on 2018-10-22 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sandesh', '0003_auto_20181022_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='Email',
            new_name='Email_Id',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='date_of_birth',
            new_name='Your_Birth',
        ),
    ]