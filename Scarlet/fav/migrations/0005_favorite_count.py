# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fav', '0004_remove_favorite_favorited'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
