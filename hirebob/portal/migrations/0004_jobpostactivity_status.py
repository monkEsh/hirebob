# Generated by Django 2.0.6 on 2018-06-05 10:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20180605_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpostactivity',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
