# Generated by Django 4.2 on 2023-04-15 00:55

from django.db import migrations, models
import talaba_s.models


class Migration(migrations.Migration):

    dependencies = [
        ('talaba_s', '0004_remove_baholar_ball_remove_baholar_semestr'),
    ]

    operations = [
        migrations.AddField(
            model_name='baholar',
            name='ball',
            field=models.SmallIntegerField(default=2, validators=[talaba_s.models.Baholar.validate_ball], verbose_name='Baho'),
        ),
        migrations.AddField(
            model_name='baholar',
            name='semestr',
            field=models.SmallIntegerField(default=1, validators=[talaba_s.models.Baholar.validate_semestr], verbose_name='Semestr'),
        ),
    ]
