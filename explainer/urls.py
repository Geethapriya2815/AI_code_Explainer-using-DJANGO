from django.urls import path
from . import views

urlpatterns = [
    path('explain/', views.explain_code, name='explain_code'),
    path('history/', views.explanation_history, name='explanation_history'),
]