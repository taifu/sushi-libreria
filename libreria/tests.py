from django.test import TestCase

# Create your tests here.

from .models import Libro, Genere, Autore

class LibroTestCase(TestCase):
    def setUp(self):
        self.romanzo = Genere.objects.create(descrizione="romanzo")
        self.suskind = Autore.objects.create(cognome="Suskind", nome="Patrick")

    def test_lista_generi(self):
        self.assertEqual(unicode(Genere.objects.all()),
                "[<Genere: romanzo>]")

    def test_serve_genere(self):
        from django.db.utils import IntegrityError
        self.assertRaises(IntegrityError, Libro.objects.create, **{"titolo": "Il Profumo"})

    def test_aggiungi_autore(self):
        libro = Libro.objects.create(titolo="Il Profumo", genere=self.romanzo)
        self.assertEqual(libro.autori.count(), 0)
        libro.autori.add(self.suskind)
        self.assertEqual(libro.autori.count(), 1)

class RicercaTestCase(TestCase):
    def test_form(self):
        from libreria.views_wiki import WikisearchForm
        form = WikisearchForm()
        self.assertIn(u"""<label for="id_autore">""", form.as_p())
