# Generated by Django 4.1.3 on 2023-04-16 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0003_remove_testdata_topic_testdata_topicdescription_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testdata',
            old_name='type',
            new_name='testType',
        ),
    ]
