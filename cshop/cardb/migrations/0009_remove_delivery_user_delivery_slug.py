# Generated by Django 4.2.7 on 2023-12-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardb', '0008_delivery_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='user',
        ),
        migrations.AddField(
            model_name='delivery',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
