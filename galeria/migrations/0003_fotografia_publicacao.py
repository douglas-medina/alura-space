# Generated by Django 5.0 on 2023-12-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicacao',
            field=models.BooleanField(default=False),
        ),
    ]
