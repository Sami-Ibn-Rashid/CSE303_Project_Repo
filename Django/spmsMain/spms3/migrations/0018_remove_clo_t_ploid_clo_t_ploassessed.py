# Generated by Django 4.1.3 on 2022-12-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spms3', '0017_clo_t_ploid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clo_t',
            name='PLOID',
        ),
        migrations.AddField(
            model_name='clo_t',
            name='PLOAssessed',
            field=models.CharField(default='PLO', max_length=50),
        ),
    ]