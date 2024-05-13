# Generated by Django 4.2.1 on 2024-05-12 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_supply_client_supplychain_contractor_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="supply",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.date(2024, 5, 13), verbose_name="Крайний срок"
            ),
        ),
        migrations.AlterField(
            model_name="cargo",
            name="height",
            field=models.FloatField(default=0, verbose_name="Высота (м)"),
        ),
        migrations.AlterField(
            model_name="cargo",
            name="length",
            field=models.FloatField(default=0, verbose_name="Длина (м)"),
        ),
        migrations.AlterField(
            model_name="cargo",
            name="units",
            field=models.CharField(
                choices=[
                    ("кг", "килограммы"),
                    ("шт", "штуки"),
                    ("л", "литры"),
                    ("паллет", "паллет"),
                ],
                default="шт",
                verbose_name="Единицы измерения",
            ),
        ),
        migrations.AlterField(
            model_name="cargo",
            name="weight",
            field=models.FloatField(default=0, verbose_name="Вес (кг)"),
        ),
        migrations.AlterField(
            model_name="cargo",
            name="width",
            field=models.FloatField(default=0, verbose_name="Ширина (м)"),
        ),
    ]