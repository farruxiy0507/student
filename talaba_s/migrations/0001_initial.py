# Generated by Django 4.2 on 2023-04-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakultet', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Fakultetlar',
            },
        ),
    ]
