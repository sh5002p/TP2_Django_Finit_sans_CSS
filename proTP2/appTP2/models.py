from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=100)

    auteur = models.CharField(max_length = 100)

    date_parution = models.DateField(blank=True, null = True)

    nombre_pages = models.IntegerField(blank=False)

    resume = models.TextField(null = True, blank = True)

    def __str__(self):

        chaine = f"{self.titre}␣écrit␣par␣{self.auteur}␣édité␣le␣{self.date_parution}"

        return chaine
