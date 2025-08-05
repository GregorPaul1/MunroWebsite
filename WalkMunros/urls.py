from django.urls import path
from WalkMunros import views

app_name = 'WalkMunros'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]