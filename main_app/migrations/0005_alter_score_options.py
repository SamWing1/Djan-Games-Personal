# Generated by Django 4.1.4 on 2022-12-24 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_score_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-value']},
        ),
    ]
