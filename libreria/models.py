from django.db import models

# Create your models here.

class Autore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)

    def __unicode__  (self):
        return u"{0} {1}".format(self.nome, self.cognome)

    class Meta:
        verbose_name_plural = "Autori"

class Genere(models.Model):
    descrizione = models.CharField(max_length=30)

    def __unicode__  (self):
        return u"{0}".format(self.descrizione)

    class Meta:
        verbose_name_plural = "Generi"

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    genere = models.ForeignKey(Genere)
    autori = models.ManyToManyField(Autore)
    data_acquisto = models.DateField(null=True, verbose_name="data di acquisto")

    def __unicode__  (self):
        return u"{0}".format(self.titolo)

    class Meta:
        verbose_name_plural = "Libri"
