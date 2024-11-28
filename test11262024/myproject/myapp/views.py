from django.shortcuts import render
import random, json

# Create your views here.
def home(request):
    return render(request, 'base.html')

def globe_view(request):
    # We no longer need to generate random heights
    # Instead, we'll pass the country colors to the template
    country_colors = {
        "United States": "#808080",
        "India": "#808080",
        "Poland": "#808080",
        "China": "#808080",
        "Mexico": "#808080"
    }
    
    # Convert the dictionary to a JSON string
    country_colors_json = json.dumps(country_colors)
    
    return render(request, 'globe.html', {'country_colors': country_colors_json})