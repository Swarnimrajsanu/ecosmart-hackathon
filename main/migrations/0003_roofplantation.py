# Generated by Django 5.1.7 on 2025-03-10 11:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_chatmessage_wasteclassification"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoofPlantation",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=200)),
                (
                    "area",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Area in square meters",
                        max_digits=10,
                    ),
                ),
                (
                    "plant_types",
                    models.TextField(
                        help_text="Types of plants used in this plantation"
                    ),
                ),
                (
                    "benefits",
                    models.TextField(
                        help_text="Environmental and social benefits of this plantation"
                    ),
                ),
                ("implementation_date", models.DateField()),
                ("maintenance_tips", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="roof_plantations/"
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "contact_phone",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("is_featured", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
