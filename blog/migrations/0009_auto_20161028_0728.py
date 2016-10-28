# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161028_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titleone',
            new_name='alt_image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imageone',
            new_name='image_dog',
        ),
        migrations.AddField(
            model_name='post',
            name='alt_image_dog',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
