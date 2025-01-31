# Generated by Django 2.2.15 on 2021-01-18 05:30
  
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0113_custom_checker_uploader'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='is_weighted',
            field=models.BooleanField(db_index=True, default=True, help_text='Whether users should earn points from this problem.', verbose_name='weighted for points'),
        ),
    ]