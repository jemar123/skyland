from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedrooms_choices, price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedrooms_choices': bedrooms_choices,
        'listings': listings
    }

    return render(request, 'pages/index.html', context)

def about(request):
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    realtors = Realtor.objects.all()

    context = {
        'mvp_realtors': mvp_realtors,
        'realtors': realtors
    }

    return render(request, 'pages/about.html', context)