# Generated by Django 2.2.14 on 2020-07-24 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_remove_contents_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contents',
            name='slug',
        ),
    ]
