from django.urls import path
from . import views

urlpatterns = [
    path('total-votes/', views.calculate_total_votes, name='total-votes'),
]