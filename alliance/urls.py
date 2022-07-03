from django.urls import path

from . import views

app_name = 'alliance'
urlpatterns = [
    path('', views.AllianceIndexView.as_view(), name='index'),
    path('<int:pk>/', views.AllianceDetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.AllianceResultsView.as_view(), name='results'),
]
