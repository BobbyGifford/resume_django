# Generated by Django 2.1.2 on 2019-01-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_project_live_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='rank',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]