from django.urls import path
from rest_framework import routers, urlpatterns
from .views import home

router = routers.DefaultRouter()

urlpatterns = [
    path("", home, name="home"),
]

urlpatterns += router.urls
