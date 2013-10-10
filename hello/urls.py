from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', "hello.views.hello"),
    url(r'^libri/$', "libreria.views.libri"),
    url(r'^libro/(\d+)/$', "libreria.views.libro"),
    url(r'^libri/acquistati/(?P<anno>\d{4})/(?P<mese>\d{1,2})/$',
        "libreria.views.libri_per_data_acquisto"),
    url(r'^libri/autori/(\d+)/$', "libreria.views.libri_autore"),
    url(r'^libri/generi/(\d+)/$', "libreria.views.libri_genere"),

    url(r'^libri/ricerca/$', "libreria.views_wiki.ricerca"),

)
