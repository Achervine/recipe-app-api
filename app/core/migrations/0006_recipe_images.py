# Generated by Django 3.2.25 on 2024-04-20 21:07

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20240420_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='images',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]
