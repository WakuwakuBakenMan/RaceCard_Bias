# Generated by Django 4.1.6 on 2024-05-30 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Race",
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
                ("date", models.DateField()),
                ("location", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Horse",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("weight", models.FloatField()),
                ("odds", models.FloatField()),
                ("popularity", models.IntegerField()),
                ("jockey", models.CharField(max_length=100)),
                ("trainer", models.CharField(max_length=100)),
                ("body_weight", models.IntegerField()),
                ("body_weight_change", models.IntegerField()),
                (
                    "race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="race_app.race"
                    ),
                ),
            ],
        ),
    ]
