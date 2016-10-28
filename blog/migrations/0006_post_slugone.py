# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_titleone'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slugone',
            field=models.SlugField(max_length=250, unique_for_date='publish', default=0),
            preserve_default=False,
        ),
    ]
