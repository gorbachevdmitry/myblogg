# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_imageone'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bodyone',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
