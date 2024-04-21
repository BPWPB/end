from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name="login_page"),
]
