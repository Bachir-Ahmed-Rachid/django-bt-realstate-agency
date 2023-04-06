from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
from .choices import state_choice,bedroom_choices,price_choice

# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'listings':page_obj,
        
    }
    return render(request,'listings/listings.html',context)
def listing(request,id):
    listing=get_object_or_404(Listing,pk=id)
    context={
        'listing':listing,
        
    }
    return render(request,'listings/listing.html',context)
def search(request):
    query_listings=Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            query_listings=query_listings.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            query_listings=query_listings.filter(city__iexact=city)
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            query_listings=query_listings.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            query_listings=query_listings.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            query_listings=query_listings.filter(price__lte=price)

    context={
        'state_choice':state_choice,
        'bedroom_choices':bedroom_choices,
        'price_choice':price_choice,
        'listings':query_listings,
        'values':request.GET
        }
    return render(request,'listings/search.html',context)