# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextFieldTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.TextField()),
                ('context', models.TextField()),
            ],
        ),
    ]