# Generated by Django 3.0.5 on 2020-04-29 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sergiu_website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
