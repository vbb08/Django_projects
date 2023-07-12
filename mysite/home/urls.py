from django.urls import path
from . import views
from django.views.generic import TemplateView
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('owner', views.owner, name='owner'),
]