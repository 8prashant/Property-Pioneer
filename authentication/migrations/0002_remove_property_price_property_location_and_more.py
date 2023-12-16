# Generated by Django 4.1.4 on 2023-01-05 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='price',
        ),
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
