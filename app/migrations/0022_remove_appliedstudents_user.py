# Generated by Django 4.2.4 on 2023-10-16 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_appliedstudents_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedstudents',
            name='user',
        ),
    ]
