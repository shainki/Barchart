# Generated by Django 3.0.6 on 2020-05-15 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSPlatform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='Score',
        ),
    ]