# Generated by Django 4.0.3 on 2023-05-19 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0010_segment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Point',
        ),
        migrations.RemoveField(
            model_name='segment',
            name='linestring',
        ),
        migrations.DeleteModel(
            name='LineString',
        ),
        migrations.DeleteModel(
            name='Segment',
        ),
    ]