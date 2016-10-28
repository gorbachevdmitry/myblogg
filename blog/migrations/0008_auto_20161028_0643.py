# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_slugone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='bodyone',
            new_name='anecdot',
        ),
        migrations.AddField(
            model_name='post',
            name='citata',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
