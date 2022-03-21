from django.urls import path
from . import views

urlpatterns = [
  path('get/', views.cookies_view)
]