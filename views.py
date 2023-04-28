from django.shortcuts import render
import requests

# Create your views here.

def index(request):



    url = 'https://newsapi.org/v2/everything?q=boxing&from=2023-04-08&sortBy=popularity&apiKey=12c5370cdafe48d090408f4b1a33f9cf'

    crypto_news = requests.get(url).json()

    a = crypto_news['articles']
    desc =[]
    title =[]
    img =[]

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(title, desc, img)

    context = {'mylist': mylist}

    return render(request, 'index.html', context)