from django.contrib import admin

# Register your models here.

from .models import Libro, Genere, Autore

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'genere', 'data_acquisto')
    
admin.site.register(Libro, LibroAdmin)
admin.site.register(Genere)
admin.site.register(Autore)
