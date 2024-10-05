from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('total-votes/', views.calculate_total_votes, name='total-votes'),
]