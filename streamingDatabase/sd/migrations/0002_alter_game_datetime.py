# Generated by Django 4.1.5 on 2023-02-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sd", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="datetime",
            field=models.DateTimeField(null=True),
        ),
    ]
