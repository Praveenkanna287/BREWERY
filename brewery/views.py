from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Brewery, Review
from .forms import ReviewForm, SignUpForm
import requests
from django.shortcuts import redirect, reverse
import uuid

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('search')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def search(request):
    query = request.GET.get('query')
    breweries = []
    if query:
        response = requests.get(f'https://api.openbrewerydb.org/breweries/search?query={query}')
        breweries = response.json()
        print(breweries)
    return render(request, 'search.html', {'breweries': breweries})

def brewery_detail(request, brewery_id):
    brewery = get_object_or_404(Brewery, id=brewery_id)
    reviews = brewery.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.brewery = brewery
            review.save()
            return redirect('brewery_detail', brewery_id=brewery.id)
    else:
        form = ReviewForm()
    return render(request, 'brewery_detail.html', {'brewery': brewery, 'reviews': reviews, 'form': form})



def generate_and_redirect(request):
    new_uuid = uuid.uuid4()
    print(new_uuid)
    return redirect(reverse('brewery_detail', args=[new_uuid]))

