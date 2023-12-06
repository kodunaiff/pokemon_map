from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Назв. на русском', max_length=200)
    description = models.TextField(verbose_name="Описание", blank=True, default="")
    image = models.ImageField(verbose_name='Картинка', null=True, blank=True)
    title_en = models.CharField(verbose_name='Назв. на английском', max_length=200, blank=True, default="")
    title_jp = models.CharField(verbose_name='Назв. на японском', max_length=200, blank=True, default="")
    previous_evolution = models.ForeignKey(
        "self", verbose_name="Прошлая эволюция", on_delete=models.CASCADE,
        null=True, blank=True, related_name="next_evolution")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появился в:', null=True)
    disappeared_at = models.DateTimeField(verbose_name='Исчез в:', null=True)
    level = models.IntegerField(verbose_name='Уровень', blank=True, default=0)
    health = models.IntegerField(verbose_name='Здоровье', blank=True, default=0)
    strength = models.IntegerField(verbose_name='Атака', blank=True, default=0)
    defence = models.IntegerField(verbose_name='Защита', blank=True, default=0)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True, default=0)
