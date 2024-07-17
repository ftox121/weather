from django.urls import path

from weatherapp.views import home, autocomplete

app_name = 'weatherapp'

urlpatterns = [
    path('', home, name='home'),
    path('autocomplete/', autocomplete, name='autocomplete'),
]