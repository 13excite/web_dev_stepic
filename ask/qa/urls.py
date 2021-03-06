from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask.qa.views import test

urlpatterns = patterns('',
    url(r'^$', test, name='test'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/\d+/', test, name='question'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
    url(r'^new/', test, name='new'),
    url(r'^admin/', admin.site.urls),
)