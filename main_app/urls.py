from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='Login_home'),
    path('home', views.app_home, name='app_home'),
    path('add', views.add, name='title_add'),

]
