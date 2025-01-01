from django.urls import path
from puzzle import views

urlpatterns = [
    path('run-simulation/', views.RunSimulationView.as_view(), name='run_simulation'),   
]
