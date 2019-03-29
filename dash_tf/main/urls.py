from django.urls import include, path
from . import views

urlpatterns = [
    path('test', views.Test.as_view(), name='test'),
]
