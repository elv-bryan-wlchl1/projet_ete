from django.conf import settings
from django.db import models
from django.utils import timezone


class Drogue(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    drogue_nom = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.drogue_nom


class Risque(models.Model):
    drogue_lien = models.ForeignKey(Drogue, on_delete=models.CASCADE)
    nombre_risque = models.IntegerField("Nombre de risques", default=0)

    @property
    def nombre_risque_nom(self):
        return "%s - %s" % (self.drogue_lien.drogue_nom, self.nombre_risque)


class Asso_Risq_Drog(models.Model):
    drogue_lien = models.ForeignKey(Drogue, on_delete=models.CASCADE)
    risque_lien = models.ForeignKey(Risque, on_delete=models.CASCADE)
    liste_risques = models.TextField("Liste de risques", max_length=200)