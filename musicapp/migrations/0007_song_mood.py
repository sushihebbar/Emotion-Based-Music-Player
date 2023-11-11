# Generated by Django 4.2.7 on 2023-11-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("musicapp", "0006_alter_playlist_id_alter_recent_id_alter_song_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="mood",
            field=models.CharField(
                choices=[
                    ("happy", "happy"),
                    ("sad", "sad"),
                    ("angry", "angry"),
                    ("disgust", "disgust"),
                    ("fear", "fear"),
                    ("surprise", "surprise"),
                    ("neutral", "neutral"),
                ],
                default="happy",
                max_length=20,
            ),
        ),
    ]
