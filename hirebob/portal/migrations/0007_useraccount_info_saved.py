# Generated by Django 2.0.6 on 2018-06-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20180605_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='info_saved',
            field=models.TextField(default='1', max_length=1),
        ),
    ]