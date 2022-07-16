# Generated by Django 4.0.6 on 2022-07-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=128, null=True, unique=True)),
                ('description', models.TextField(max_length=512)),
                ('category', models.CharField(max_length=64)),
                ('url', models.URLField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio_images/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]