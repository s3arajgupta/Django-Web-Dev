# Generated by Django 3.0 on 2019-12-16 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='summary',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='000', max_length=255),
        ),
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]