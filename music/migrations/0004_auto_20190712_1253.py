# Generated by Django 2.2.2 on 2019-07-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190711_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
