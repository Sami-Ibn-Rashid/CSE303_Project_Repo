# Generated by Django 4.1.3 on 2022-12-07 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMAS', '0005_remove_clo_courseid_section_courseid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courseevaluation',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='courselesson',
            unique_together=set(),
        ),
    ]
