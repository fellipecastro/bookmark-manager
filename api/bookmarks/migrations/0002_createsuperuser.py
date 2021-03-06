# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.admin import User


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@example.com'
    superuser.set_password('q1w2e3r4')
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
