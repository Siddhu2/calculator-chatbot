from django.urls import path
from arithmetic import views

urlpatterns = [
    path('', views.home, name="home"),
    path('webhook/', views.webhook, name='webhook'),
]