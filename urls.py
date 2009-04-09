from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^vvsr/', include('vvsr.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^kml/$', 'vvsr.mapping.views.all_kml'),
    (r'^map/$', 'vvsr.mapping.views.show_map'),
    (r'^$', 'vvsr.mapping.views.show_map'),
    (r'^json/heritage/', 'vvsr.mapping.views.getObjJson'),
    (r'^admin/(.*)', admin.site.root),
    )

if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)/$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )

