# Generated by Django 4.0.3 on 2022-03-25 13:50

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_blog_image_alter_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='estlove.jpeg', upload_to=api.models.upload_image_path),
        ),
    ]
