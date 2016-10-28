# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_bodyone'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titleone',
            field=models.CharField(max_length=250, default=0),
            preserve_default=False,
        ),
    ]
