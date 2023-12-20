from django.shortcuts import render, HttpResponse , redirect
import http
import requests
API_KEY = '8f70a9bce48c4a8d93552d50d58ecbd9'


# Create your views here.

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        #print(data)
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'Newspage.html', context)

def homepage(request):

  #return render(request, 'Newspage.html')
  return HttpResponse("work")
