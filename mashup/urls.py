from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'yodasms.views.home', name='home'),
    url(r'^sent/$', 'yodasms.views.sent', name='sent'),

    url(r'^admin/', include(admin.site.urls)),
)
