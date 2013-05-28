from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	(r'^twitter/', include('twython_django_oauth.urls')),
    url(r'^$', include("project.authsystem.urls")),
    (r'^facebook_connect/', include('facebook_connect.urls')),
)
