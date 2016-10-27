# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161026_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageone',
            field=models.ImageField(upload_to='posts/%Y/%m/%d', blank=True),
        ),
    ]
