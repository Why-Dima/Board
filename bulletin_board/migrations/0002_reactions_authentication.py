# Generated by Django 4.0.5 on 2022-06-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='authentication',
            field=models.BooleanField(default=False),
        ),
    ]
