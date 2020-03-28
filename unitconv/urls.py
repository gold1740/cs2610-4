from django.urls import path

from . import views

urlpatterns = [
    path('', views.convert ),
    path('convert', views.convert),
]
