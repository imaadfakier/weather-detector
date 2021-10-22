from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        response = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q={the_city}+&appid=82a4524ab33c403ffff483dd034f0f53'
            .format(the_city=city)
        ).read()
        data = json.loads(response)
        # print(str(data['main']['temp']))
        dict_data = {
            'country_code': str(data['sys']['country']), 
            'coordinate': str(data['coord']['lon']) + ' ' + str(data['coord']['lat']), 
            'temperature': str(data['main']['temp']) + 'k(elvin)', 
            'pressure': str(data['main']['pressure']), 
            'humidity': str(data['main']['humidity']),
        }
        return render(request, 'index.html', {'city': city, 'the_data': dict_data})
    return render(request, 'index.html')