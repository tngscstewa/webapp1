from django.contrib import admin
from matapp.views import *
from matpro.settings import *
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', 'matapp.views.log', name='log'),
    url(r'^$', userform.as_view(),name='userform'),
    url(r'^adv_info/$', advform.as_view(),name='advform'),
    url(r'^fulldet/(?P<pk>[-\w]+)/$', fulldet.as_view()),
    url(r'^dummy/$', 'matapp.views.dummy',name='dummy'),
    url(r'^logout/$', 'matapp.views.user_logout',name='logout'),
    url(r'^approve/(?P<pk>[-\w]+)/$', approve.as_view()),
    url(r'^delete/(?P<pk1>[-\w]+)/(?P<pk2>[-\w]+)/(?P<pk3>[-\w]+)/(?P<pk4>[-\w]+)/$', delete.as_view()),
    url(r'^search/$', 'matapp.views.search',name='search'),
    
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),    
)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=staticfiles_urlpatterns()
