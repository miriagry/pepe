from django.shortcuts import render
from random import randint
from .models import Quote

def index(request):
    counter = Quote.objects.all().count()
    ri = randint(0, counter - 1)
    context = {'quote' : Quote.objects.all()[ri]}
    return render(request, 'random_quote.html', context)
# Create your views here.
