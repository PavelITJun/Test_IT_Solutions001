# Generated by Django 4.2.14 on 2024-07-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Advertisement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("ad_id", models.IntegerField(unique=True)),
                ("author", models.CharField(max_length=255)),
                ("views", models.IntegerField(default=0)),
                ("position", models.IntegerField()),
            ],
        ),
    ]
