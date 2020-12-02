from libreria.models import *

romanzo = Genere.objects.create(descrizione="romanzo")
fantascienza = Genere.objects.create(descrizione="fantascienza")
giallo = Genere.objects.create(descrizione="giallo")
suskind = Autore.objects.create(cognome="Suskind", nome="Patrick")
asimov = Autore.objects.create(cognome="Asimov", nome="Isaac")
ellroy = Autore.objects.create(cognome="Ellroy", nome="James")
profumo = Libro.objects.create(titolo="Il Profumo", genere=romanzo)
profumo.autori.add(suskind)
dalia = Libro.objects.create(titolo="La dalia nera", genere=giallo)
dalia.autori.add(ellroy)
fondazione = Libro.objects.create(titolo="Fondazione", genere=fantascienza)
fondazione.autori.add(asimov)
