from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('index.html', views.index, name='index'), 
    path('aboutme.html', views.aboutme, name='aboutme'), 
    path('emoji.html', views.emoji, name='emoji'), 
    path('gallery.html', views.gallery, name='gallery'), 
    path('links.html', views.links, name='links'), 
        path('shop.html', views.shop, name='index'), 
        path('calendar.html', views.calendar, name='calendar'), 
        path('rclinic.html', views.rclinic, name='rlcinic'),
        path('rclinic2.html', views.rclinic2, name='rclinic2'),  
        path('scheduler.html', views.scheduler, name='scheduler'),
        path('logout/', views.user_logout, name="logout"),
        path('user_login.html', views.user_login, name="login"),
        path('user_register.html', views.user_register, name="register")
]
