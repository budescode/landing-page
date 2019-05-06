from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views

urlpatterns = [
    path('', views.home, name="home" ),
	# url(r'^$', core_views.home, name='home'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
]




