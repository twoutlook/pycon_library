from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'pycon_library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^libadmin/', include(admin.site.urls)),
]
