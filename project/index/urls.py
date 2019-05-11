from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='home'
urlpatterns = [
    path('', views.home, name="home" ),
	path('register-seeker/', views.register_seeker, name="register_seeker" ),
	path('register-poster/', views.register_poster, name="register_poster" ),
	path('post/', views.post, name="post" ),
	path('login/', views.login_page, name="login" ),
	path('loginpage/', views.login_view, name="login_view" ),
	path('logout/', views.logout_page, name="logout_page" ),
	path('filter/', views.search_field, name="search_field" ),
	# url(r'^$', core_views.home, name='home'),
	# url(r'^login/$', auth_views.login, name='login'),
	# path('login/', views.login, name="login" ),
	# url(r'^login/$', auth_views.login, name='login'),
	# url(r'^logout/$', auth_views.logout, name='logout'),

]



