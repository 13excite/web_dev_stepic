from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask.qa.views import test


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('qa.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/[0-9]+/', test),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test),
)