# Generated by Django 4.0.4 on 2022-08-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(default=None, upload_to='image'),
        ),
    ]
