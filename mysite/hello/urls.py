'''from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.hello),
]
'''
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'hello'
urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    path('owner', views.owner, name='owner'),
]