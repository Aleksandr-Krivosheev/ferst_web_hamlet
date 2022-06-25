from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('abo', views.about, name='about'),
    path('ab-br', views.about_prices, name='about_prices'),
    path('abstract', views.abstract , name='abstract'),
    path('authors', views.authors, name='authors'),
    path('basket', views.basket, name='basket'),
    path('bookinisted', views.bookinisted, name='bookinisted'),
    path('cd_and_dvd', views.cd_and_dvd, name='cd_and_dvd'),
    path('contacts', views.contacts, name='contacts'),
    path('feedback', views.feedback, name='feedback'),
    path('month', views.month, name='month'),
    path('order', views.order, name='order'),
    path('subscription', views.subscription, name='subscription'),
    path('tags', views.tags, name='tags'),
    path('theonlyone', views.theonlyone, name='theonlyone'),
]

