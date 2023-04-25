import folium

from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils import timezone
from django.shortcuts import get_object_or_404


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons = Pokemon.objects.all()
    for pokemon_entity in PokemonEntity.objects.filter(
            appeared_at__lte=timezone.localtime(),
            disappeared_at__gte=timezone.localtime()):
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(
                pokemon_entity.pokemon.image.url
            )
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
                    'pokemon_id': pokemon.id,
                    'img_url': request.build_absolute_uri(
                        pokemon.image.url
                    ),
                    'title_ru': pokemon.title,
                })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    next_evolution = {}
    previous_evolution = {}

    next_evolution_pokemon = pokemon.next_evolution
    if next_evolution_pokemon:
        next_evolution = {
            "title_ru": next_evolution_pokemon.title,
            "pokemon_id": next_evolution_pokemon.id,
            "img_url": request.build_absolute_uri(
                next_evolution_pokemon.image.url
            )
        }

    previous_evolution_pokemon = pokemon.previous_evolutions.all().first()
    if previous_evolution_pokemon:
        previous_evolution = {
            "title_ru": previous_evolution_pokemon.title,
            "pokemon_id": previous_evolution_pokemon.id,
            "img_url": request.build_absolute_uri(
                previous_evolution_pokemon.image.url
            )
        }

    pokemon_serialized = {"img_url": request.build_absolute_uri(pokemon.image.url),
                    "title_ru": pokemon.title,
                    "description": pokemon.description,
                    "title_jp": pokemon.title_jp,
                    "title_en": pokemon.title_en,
                    "next_evolution": next_evolution,
                    "previous_evolution": previous_evolution
                    }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon):
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.image.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_serialized
    })
