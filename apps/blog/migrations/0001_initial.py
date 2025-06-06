# Generated by Django 5.2 on 2025-04-27 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articulo",
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
                ("autor", models.CharField(max_length=100)),
                ("nombre", models.CharField(max_length=200)),
                ("resumen", models.TextField()),
                ("version_ciencia", models.TextField()),
                ("version_difusion", models.TextField()),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("psicologia", "Psicología"),
                            ("ciencia", "Ciencia"),
                            ("opinion", "Opinión"),
                            ("ia", "IA"),
                            ("software", "Software"),
                            ("otro", "Otro"),
                        ],
                        max_length=20,
                    ),
                ),
                ("slug", models.SlugField(blank=True, max_length=220, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ImagenArticulo",
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
                ("imagen", models.ImageField(upload_to="articulos/")),
                (
                    "descripcion",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "articulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="imagenes",
                        to="blog.articulo",
                    ),
                ),
            ],
        ),
    ]
