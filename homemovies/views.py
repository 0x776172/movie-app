from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers

import json

from homemovies.models import Movie

# Create your views here.
def index(request):
    print("index")
    movie_list = Movie.objects.order_by('id')
    context = {
        "movie_list": movie_list,
    }
    return render(request, "home/home.html", context)

def get_by_name(request):
    id = request.GET.get("name")
    try:
        movie_list = Movie.objects.filter(name__contains=id)
        print(movie_list)
        context = {
            "movie_list": movie_list.filter()
        }
        return JsonResponse(loader.render_to_string("home/home_search.html", context), safe=0)
    except Exception as e:
        return JsonResponse({"error": str(e)})

def detail(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        return HttpResponse("Error")
    genre = movie.genre.replace('[', "").replace(']', '').replace("'", '')
    mpaarating = json.loads(movie.mpaarating.replace("'", '"'))
    context = { 
        "movie": movie, 
        "genre": genre,
        "type": mpaarating["type"],
        "label": mpaarating["label"]
        }
    return render(request, "detail/detail.html", context)