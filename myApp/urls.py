from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.homepage),
    path('result/', views.result, name="result")
]