# Generated by Django 2.0.6 on 2018-06-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20180605_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gmail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
