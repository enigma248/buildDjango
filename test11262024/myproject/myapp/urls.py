from django.urls import path
from .views import home, globe_view

urlpatterns = [
    path('', home, name='home'),
    path('globe/', globe_view, name='globe'),
]