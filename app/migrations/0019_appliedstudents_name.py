# Generated by Django 4.2.4 on 2023-10-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_appliedstudents_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedstudents',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
