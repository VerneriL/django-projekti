from django.db import models


class Tuote(models.Model):
    nimi = models.CharField(max_length=100)

    def __str__(self):
        return f"Tuote: {self.nimi}"
