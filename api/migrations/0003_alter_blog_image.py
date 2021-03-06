# Generated by Django 4.0.3 on 2022-03-15 13:28

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=api.models.upload_image_path),
            preserve_default=False,
        ),
    ]
