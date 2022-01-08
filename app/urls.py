from django.urls import path
from .views import Web_hizmat

app_name = 'app'

urlpatterns = [
    path("", Web_hizmat, name="Home")
]
