from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(0, 'Adicione um valor maior que 0'),
                                            MaxValueValidator(5, 'Adicione um valor menor que 5')])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie}'
