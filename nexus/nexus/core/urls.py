from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('setting', views.settings, name='setting'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('upload', views.upload, name='upload'),
    path('logout', views.Logout, name='logout'),
    path('profile', views.profile, name='profile'),


]