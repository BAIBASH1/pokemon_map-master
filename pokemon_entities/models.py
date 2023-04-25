from django.db import models


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="имя"
    )
    title_en = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="имя на английском"
    )
    title_jp = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="имя на японском"
    )

    image = models.ImageField(
        blank=True,
        verbose_name="фотография",
        default=""
    )

    description = models.TextField(
        blank=True,
        verbose_name="описание"
    )

    next_evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="previous_evolutions",
        verbose_name="следующая эволюция"
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name="какой покемон",
        related_name="pokemon_entities"
    )

    lat = models.FloatField(verbose_name="широта")
    lon = models.FloatField(verbose_name="долгота")

    appeared_at = models.DateTimeField(
        blank=True, null=True,
        verbose_name="время появления"
    )
    disappeared_at = models.DateTimeField(
        blank=True, null=True,
        verbose_name="время исчезновения"
    )

    level = models.IntegerField(
        blank=True, null=True,
        verbose_name="уровень"
    )
    health = models.IntegerField(
        blank=True, null=True,
        verbose_name="здоровье"
    )
    strength = models.IntegerField(
        blank=True, null=True,
        verbose_name="сила"
    )
    defence = models.IntegerField(
        blank=True, null=True,
        verbose_name="защита"
    )
    stamina = models.IntegerField(
        blank=True, null=True,
        verbose_name="выносливость"
    )

    def __str__(self):
        return f"{self.pokemon}, id={self.pokemon.id}"
