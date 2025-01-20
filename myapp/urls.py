from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('division/<str:division>/', views.mark_attendance, name='mark_attendance'),
    path('reports/<str:division>/', views.reports, name='reports'),
]
