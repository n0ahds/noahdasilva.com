# Generated by Django 4.0.5 on 2022-07-14 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_user_first_name_remove_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=24, unique=True, verbose_name='username'),
        ),
    ]
