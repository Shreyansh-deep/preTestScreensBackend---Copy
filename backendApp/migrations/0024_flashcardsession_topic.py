# Generated by Django 4.1.3 on 2023-09-24 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0023_remove_flashcardsession_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcardsession',
            name='topic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backendApp.flashcardtopic'),
            preserve_default=False,
        ),
    ]
