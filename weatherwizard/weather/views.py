import requests
from django.shortcuts import render # type: ignore

def home(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'dd13aca4f70a22afdfd9255f4fdefe31'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        print(data)

        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed'],
            }

    return render(request, 'home.html', {'weather': weather_data})
