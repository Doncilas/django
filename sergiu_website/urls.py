from django.urls import path
from .views import index, help_me

urlpatterns = [
    path('', index, name='index'),
    path('help/', help_me, name='help_me')

]

