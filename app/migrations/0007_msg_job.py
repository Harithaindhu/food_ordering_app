# Generated by Django 4.0.4 on 2022-08-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_msg_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='job',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]