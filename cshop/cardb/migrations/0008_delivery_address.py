# Generated by Django 4.2.7 on 2023-12-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardb', '0007_delivery_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='address',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
