# Generated by Django 4.0.5 on 2022-07-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_rename_timestamp_auditentry_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='failed_login_attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='previous_failed_login_attempts',
            field=models.IntegerField(default=0),
        ),
    ]
