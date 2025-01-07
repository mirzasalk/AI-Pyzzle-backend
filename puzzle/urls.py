from django.urls import path
from puzzle import views

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to the backend!")),
    path('run-simulation/', views.RunSimulationView.as_view(), name='run_simulation'),   
]
