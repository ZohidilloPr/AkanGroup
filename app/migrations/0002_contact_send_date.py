# Generated by Django 3.2.9 on 2021-12-14 04:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='send_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='SEND_TIME'),
            preserve_default=False,
        ),
    ]
