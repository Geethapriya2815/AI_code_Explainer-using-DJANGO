# ai_code_explainer/urls.py

from django.contrib import admin
from django.urls import path, include
from explainer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # custom home
    path('explain/', views.explain_code, name='explain_code'),
    path('history/', views.explanation_history, name='explanation_history'),
    path('accounts/', include('django.contrib.auth.urls')),  # built-in login/logout
]
