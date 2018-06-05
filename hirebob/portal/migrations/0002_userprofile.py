# Generated by Django 2.0.6 on 2018-06-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('gmail', models.EmailField(max_length=254)),
                ('linkedin', models.CharField(max_length=30)),
                ('skype_id', models.CharField(max_length=30)),
                ('about_me', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=200)),
                ('birthaday', models.DateField()),
                ('job_title', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
    ]