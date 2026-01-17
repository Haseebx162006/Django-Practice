from django.urls import path
from . import views
urlpatterns = [
    path("January", views.index),
    path("Feb",views.feb)
]
