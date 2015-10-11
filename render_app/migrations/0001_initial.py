# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('obj_file', models.FileField(upload_to=b'objectFile')),
                ('coordinates', models.CharField(max_length=500000, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Object',
                'verbose_name_plural': 'Objects',
            },
            bases=(models.Model,),
        ),
    ]
