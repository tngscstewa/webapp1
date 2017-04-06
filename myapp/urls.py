from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from myapp.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myapp.views.Index', name='home'),
    url(r'^state_admin_login$', view=State_login.as_view(),name='state_admin_login'),
	url(r'^about$', ('myapp.views.About'),name='about_page'),
	url(r'^services$', ('myapp.views.Services'),name='services_page'),
	url(r'^message$', ('myapp.views.Message'),name='message_page'),
	url(r'^documents$', ('myapp.views.Documents'),name='documents_page'),
	url(r'^gallery$', ('myapp.views.Gallery'),name='gallery_page'),
	url(r'^membership$',view=Membership.as_view(), name='print'),
	url(r'^contact$', ('myapp.views.Contact'),name='contact_page'),
	url(r'^members_all$', ('myapp.views.Members_all'),name='members_all_page'),
	url(r'^get_id$',view=GetId.as_view(), name='print'),
	url(r'^chaining/', include('smart_selects.urls')),
    # url(r'^mysite/', include('foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)