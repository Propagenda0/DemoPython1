# Generated by Django 4.1 on 2022-10-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="2001-06-25"),
            preserve_default=False,
        ),
    ]
