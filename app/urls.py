from django.urls import path

from . import views

urlpatterns = [
               path('', views.index, name='index'),
               path('login/', views.login, name='login'),
               path('register/', views.register, name='register'),
               path('forgot-password/', views.forgot, name='forgot-password'),
               path('prices/', views.prices, name='prices'),
               path('poverty/', views.poverty, name='poverty'),
               path('updates/', views.govt_initiatives, name='updates'),
                path('404/', views.pagenotfound, name='404'),
            ]
