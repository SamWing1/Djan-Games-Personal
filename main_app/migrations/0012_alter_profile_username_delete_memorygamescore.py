# Generated by Django 4.1.4 on 2023-01-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0011_merge_0009_profile_0010_memorygamescore_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name="MemoryGameScore",
        ),
    ]