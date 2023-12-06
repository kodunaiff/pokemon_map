from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField('Назв. на русском', max_length=200)
    description = models.TextField("Описание", blank=True, default="")
    image = models.ImageField('Картинка', null=True, blank=True)
    title_en = models.CharField('Назв. на английском', max_length=200, blank=True, default="")
    title_jp = models.CharField('Назв. на японском', max_length=200, blank=True, default="")
    previous_evolution = models.ForeignKey(
        "self", verbose_name="Прошлая эволюция", on_delete=models.CASCADE,
        null=True, blank=True, related_name="next_evolution")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появился в', null=True)
    disappeared_at = models.DateTimeField('Исчез в', null=True)
    level = models.IntegerField('Уровень')
    health = models.IntegerField('Здоровье')
    strength = models.IntegerField('Атака')
    defence = models.IntegerField('Защита')
    stamina = models.IntegerField('Выносливость')
