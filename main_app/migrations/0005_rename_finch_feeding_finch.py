# Generated by Django 3.2.9 on 2022-01-12 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_feeding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeding',
            old_name='Finch',
            new_name='finch',
        ),
    ]
