from django.contrib.auth.models import User
from django.db import models


class Ads(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастер заклинаний'),
    )
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    text = models.TextField()
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    upload = models.FileField(upload_to='upload/')

    def get_absolute_url(self):
        return f'/detail/{self.id}'


class Reactions(models.Model):
    authors = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    reaction = models.TextField(max_length=500)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    authentication = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.reaction}'
