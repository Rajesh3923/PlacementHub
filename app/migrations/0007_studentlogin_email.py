# Generated by Django 4.2.4 on 2023-08-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_studentlogin_remove_studentnew_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlogin',
            name='email',
            field=models.EmailField(default='21a81a0539@gmail.com', max_length=254),
        ),
    ]