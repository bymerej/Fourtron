from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from fourtron.core.views import index, oauth, oauth_logout, oauth_error

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^oauth', oauth, name="oauth"),
    url(r'^oauth_error/$', oauth_error, name='oauth_error'),
    url(r'^oauth_logout/$', oauth_logout, name='oauth_logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)
