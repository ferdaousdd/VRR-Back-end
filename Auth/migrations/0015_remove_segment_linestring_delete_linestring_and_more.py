# Generated by Django 4.0.3 on 2023-05-19 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0014_linestring_point_segment_linestring_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segment',
            name='linestring',
        ),
        migrations.DeleteModel(
            name='LineString',
        ),
        migrations.DeleteModel(
            name='Point',
        ),
        migrations.DeleteModel(
            name='Segment',
        ),
    ]
