from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from core.views import task, landing_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectname.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', landing_page),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# enables local media serving
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)

