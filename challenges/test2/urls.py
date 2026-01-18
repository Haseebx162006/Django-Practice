from django.urls import include , path
from . import views
urlpatterns = [
    path("Jan",view=views.hello)

]
