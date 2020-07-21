from django.urls import path
from .views import calc
from . import views

urlpatterns = [
    path('calc/',views.calc.as_view()),
]