# Generated by Django 3.0.4 on 2020-03-11 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gratitudes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gratitude',
            name='date',
        ),
        migrations.RemoveField(
            model_name='gratitude',
            name='subject',
        ),
    ]
