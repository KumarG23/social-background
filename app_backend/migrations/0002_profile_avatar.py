# Generated by Django 5.0.6 on 2024-06-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
