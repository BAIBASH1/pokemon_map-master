from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    Lat = models.FloatField()
    Lon = models.FloatField()
    Appeared_at = models.DateTimeField(blank=True, null=True)
    Disappeared_at = models.DateTimeField(blank=True, null=True)
    Level = models.IntegerField(blank=True, null=True)
    Health = models.IntegerField(blank=True, null=True)
    Strength = models.IntegerField(blank=True, null=True)
    Defence = models.IntegerField(blank=True, null=True)
    Stamina = models.IntegerField(blank=True, null=True)

