# Generated by Django 4.2.5 on 2023-11-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("predict", "0011_game_bet_game_complexspread_game_ev_margin1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="gamedate",
            field=models.CharField(default="2023-11-04", max_length=10),
        ),
    ]
