# Generated by Django 3.1.14 on 2023-04-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20230423_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
