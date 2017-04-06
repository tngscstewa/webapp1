# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat', models.CharField(max_length=10, verbose_name='Category', choices=[(b'S', b'STUDENT'), (b'T', b'TEACHER')])),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=13, verbose_name='Mobile')),
                ('district', models.ForeignKey(verbose_name='District', to='matapp.District')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
