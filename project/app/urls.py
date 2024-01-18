from django.urls import path
from .views import shorten_url,redirect_to_original

urlpatterns = [
    path('',shorten_url,name="shorten"),
    path('<str:token>',redirect_to_original,name="longen")
]