from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('home', views.homepage, name ="home"),
    path('removal', views.removal, name ="removal"),
    path('splicing', views.splicing, name="splicing"),
    path('copymove', views.copymove, name = "copymove"),
    path('quiz', views.quiz, name = "quiz"),
    path('result', views.result, name="result")
]