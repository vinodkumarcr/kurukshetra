# Generated by Django 2.1.2 on 2018-10-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandesh', '0004_auto_20181022_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='sandesh_send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('sandesh', models.CharField(max_length=500)),
            ],
        ),
    ]