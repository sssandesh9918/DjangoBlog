# Generated by Django 2.2.14 on 2020-07-19 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200719_0602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contents',
            options={'ordering': ['-created_at']},
        ),
    ]
