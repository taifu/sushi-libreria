from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Libro, Autore, Genere

def libri(request):
    return render(request, 'libri.html', {
        'libri': Libro.objects.all().order_by('titolo')
    })

def libro(request, id):
    try:
        libro = Libro.objects.get(pk=id)
        return HttpResponse(u"\"{0}\" di {1}, {2}<br>".format(
                libro.titolo,
                u", ".join(unicode(autore) for autore in libro.autori.all()),
                libro.genere))
    except Libro.DoesNotExist:
        return HttpResponse("Codice %s inesistente" % id)

def libri_per_data_acquisto(request, mese, anno):
    libri = Libro.objects.filter(data_acquisto__year=int(anno))
    libri = libri.filter(data_acquisto__month=int(mese))
    elenco = ""
    for libro in libri.order_by('titolo'):
        elenco += u"\"{0}\" di {1}, {2}<br>".format(
                libro.titolo,
                u", ".join(unicode(autore) for autore in libro.autori.all()),
                libro.genere)
    if elenco == "":
        elenco = "Nessun libro"
    return HttpResponse(elenco)

def libri_genere(request, id):
  genere = get_object_or_404(Genere, pk=id)
  return render(request, 'libri.html', {
    'libri': Libro.objects.filter(
      genere=genere).order_by('titolo'),
    'genere': genere,})

def libri_autore(request, id):
  autore = get_object_or_404(Autore, pk=id)
  return render(request, 'libri.html', {
    'libri': Libro.objects.filter(
      autori=autore).order_by('titolo'),
    'autore': autore,})
