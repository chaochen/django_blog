from django.conf.urls import patterns, include, url

from django.contrib import admin
import blog_app.urls

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'blog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^blog_app/', include(blog_app.urls)),
)
