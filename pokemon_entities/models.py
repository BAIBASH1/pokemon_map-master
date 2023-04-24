from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="имя")
    title_en = models.CharField(max_length=20, blank=True, default="", verbose_name="имя на английском")
    title_jp = models.CharField(max_length=20, blank=True, default="", verbose_name="имя на японском")
    image = models.ImageField(blank=True, verbose_name="фотография")
    description = models.TextField(blank=True, default="", verbose_name="описание")
    next_evolution = models.ForeignKey("Pokemon", on_delete=models.SET_NULL, null=True, blank=True, related_name="previous_evolution", verbose_name="следующая эволюция")


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="какой покемон")
    Lat = models.FloatField(verbose_name="широта")
    Lon = models.FloatField(verbose_name="долгота")
    Appeared_at = models.DateTimeField(blank=True, null=True, verbose_name="время появления")
    Disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name="время исчезновения")
    Level = models.IntegerField(blank=True, null=True, verbose_name="уровень")
    Health = models.IntegerField(blank=True, null=True, verbose_name="здоровье")
    Strength = models.IntegerField(blank=True, null=True, verbose_name="сила")
    Defence = models.IntegerField(blank=True, null=True, verbose_name="защита")
    Stamina = models.IntegerField(blank=True, null=True, verbose_name="выносливость")

