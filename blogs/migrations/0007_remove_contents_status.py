# Generated by Django 2.2.14 on 2020-07-19 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_contents_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contents',
            name='status',
        ),
    ]
