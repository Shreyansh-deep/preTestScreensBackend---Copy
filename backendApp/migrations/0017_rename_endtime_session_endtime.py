# Generated by Django 4.1.3 on 2023-09-12 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0016_session_alter_userreaction_datetime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='EndTime',
            new_name='endTime',
        ),
    ]
