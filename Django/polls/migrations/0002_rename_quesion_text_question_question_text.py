# Generated by Django 4.1.7 on 2023-03-12 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quesion_text',
            new_name='question_text',
        ),
    ]
