from django.urls import  path

from .views import test1

urlpatterns = [
    path("", test1 , name="test" ),
]
