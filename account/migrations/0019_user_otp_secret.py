# Generated by Django 4.0.6 on 2022-08-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_user_original_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp_secret',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='otp secret'),
        ),
    ]
