import json
import urllib.request
from django.shortcuts import render
from django.http import JsonResponse
import requests

from weatherapp.models import CityQueryCount


def home(request):
    last_city = request.session.get('last_city', '')

    data = {}

    if request.method == 'POST':
        city = request.POST['city']
        request.session['last_city'] = city  # Сохраняем последний город в сессии

        try:
            source = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=1f6980c3e9caa2bf6ce2d98386de8924'
            ).read()
            list_of_data = json.loads(source)

            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
                'city': city
            }
        except KeyError:
            data = {'error': 'City not found'}
    elif last_city:
        try:
            source = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/weather?q={last_city}&units=metric&appid=1f6980c3e9caa2bf6ce2d98386de8924'
            ).read()
            list_of_data = json.loads(source)

            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
                'city': last_city
            }
        except KeyError:
            data = {'error': 'City not found'}
    return render(request, "weatherapp/home.html", data)


def autocomplete(request):
    if 'term' in request.GET:
        term = request.GET.get('term')
        api_key = '1f6980c3e9caa2bf6ce2d98386de8924'
        api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={term}&limit=5&appid={api_key}'

        try:
            response = requests.get(api_url)
            data = response.json()

            # Логирование данных ответа от API
            print("API Response:", data)

            if isinstance(data, list):
                suggestions = [city['name'] for city in data]
            else:
                suggestions = []

        except ValueError as e:
            print(f"Error parsing JSON: {e}")
            return JsonResponse([], safe=False)
        except Exception as e:
            print(f"Error during request: {e}")
            return JsonResponse([], safe=False)

        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)

