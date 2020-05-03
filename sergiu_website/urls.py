from django.urls import path
from .views import index, users

urlpatterns = [
    path('', index, name='index'),
    path('', users, name='users')

    # path('help/', help_me, name='help_me')

]

