# Generated by Django 3.0.8 on 2020-07-05 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0002_auto_20200705_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to='handler.User'),
        ),
    ]