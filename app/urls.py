from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("register_with_model_form",register_with_model_form,name="rd")
]
