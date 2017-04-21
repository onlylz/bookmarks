from django.conf.urls import url

from django.contrib.auth import views
from . import views as account_views

urlpatterns = [
    #url(r'^login/$', views.user_login, name='login'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^logout_then_login/$', views.logout_then_login, name='logout_then_login'),
    url(r'^$', account_views.dashboard, name='dashboard'),
]
