# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 10:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RATapp', '0020_auto_20170325_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='crash',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RATapp.Crash'),
        ),
        migrations.AddField(
            model_name='offer',
            name='message',
            field=models.TextField(default='', verbose_name='message'),
        ),
        migrations.AddField(
            model_name='offer',
            name='price',
            field=models.IntegerField(default=0, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='offer',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RATapp.Service'),
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(null=True, verbose_name='review_date'),
        ),
        migrations.AddField(
            model_name='review',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RATapp.Service'),
        ),
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default='', verbose_name='text'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]