# Generated by Django 3.1.3 on 2021-04-16 09:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testclass',
            name='array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=None, null=True, size=200),
        ),
    ]
