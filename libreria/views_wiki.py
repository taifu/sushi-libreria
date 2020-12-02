import urllib2
from json import JSONDecoder
from django import forms
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from models import Autore

class WikisearchForm(forms.Form):
  autore = forms.IntegerField(widget=forms.Select(
    choices = [(autore.pk, autore) for autore in
    Autore.objects.all()]))
  wikipedia = forms.CharField(widget=forms.Select(
    choices=(("it","Italiana"),
        ("en","Inglese"))))
  limite = forms.IntegerField(initial=10,
    widget=forms.RadioSelect(
        choices=((10,"10"),
            (30,"30"),
            (50,"50"))))

  def clean_limite(self):
    if (self.cleaned_data['limite'] == 50 and
        self.cleaned_data['wikipedia'] == 'en'):
      raise forms.ValidationError(
         "Massimo 30 risultati in inglese!")
    return self.cleaned_data['limite']


WIKI_URL_API = (u"http://{0}.wikipedia.org/w/api.php?"
  "action=query&format=json&srlimit={1}&"
  "list=search&srsearch={2}")
WIKI_LINK = "http://{0}.wikipedia.org/wiki/"

def ricerca(request):
  risultati = link = None
  if request.method == 'POST':
    form = WikisearchForm(request.POST)
    if form.is_valid():
      autore = get_object_or_404(Autore,
        pk=form.cleaned_data['autore'])
      url = WIKI_URL_API.format(form.cleaned_data['wikipedia'],
        form.cleaned_data['limite'],
        autore.cognome)
      link = WIKI_LINK.format(form.cleaned_data['wikipedia'])
      print url
      dati = urllib2.urlopen(url.encode('utf-8')).read()
      valori = JSONDecoder().decode(dati)
      risultati = valori['query']['search']
  else:
    form = WikisearchForm()
  return render(request, 'wikisearch.html', {
    'form': form,
    'link': link,
    'risultati': risultati,})
