# Generated by Django 4.0.3 on 2022-03-25 13:52

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='estlove.jpeg', null=True, upload_to=api.models.upload_image_path),
        ),
    ]
