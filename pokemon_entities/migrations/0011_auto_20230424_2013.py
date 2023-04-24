# Generated by Django 3.1.14 on 2023-04-24 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_pokemon_next_evolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='фотография'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolution', to='pokemon_entities.pokemon', verbose_name='следующая эволюция'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='имя на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='имя на японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Appeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Defence',
            field=models.IntegerField(blank=True, null=True, verbose_name='защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Disappeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Health',
            field=models.IntegerField(blank=True, null=True, verbose_name='здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Lat',
            field=models.FloatField(verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Level',
            field=models.IntegerField(blank=True, null=True, verbose_name='уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Lon',
            field=models.FloatField(verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='какой покемон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Strength',
            field=models.IntegerField(blank=True, null=True, verbose_name='сила'),
        ),
    ]