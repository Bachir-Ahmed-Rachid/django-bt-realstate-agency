from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choice,bedroom_choices,price_choice
from django.views.generic.base import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = "pages/index.html"
    def get_context_data(self, **kwargs):
        listing=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
        context = super().get_context_data(**kwargs)
        context['listings'] = listing
        context['state_choice'] = state_choice
        context['bedroom_choices'] = bedroom_choices
        context['price_choice'] = price_choice
        return context
    
class AboutView(TemplateView):
    template_name = "pages/about.html"
    def get_context_data(self, **kwargs):
        realtor=Realtor.objects.order_by('-hire_date')
        mvp_realtor=Realtor.objects.all().filter(is_mvp=True)
        context = super().get_context_data(**kwargs)
        context['realtors'] = realtor
        context['mvp_realtors'] = mvp_realtor
        return context





















#function base views:
def index(request):
    listing=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listing,
        'state_choice':state_choice,
        'bedroom_choices':bedroom_choices,
        'price_choice':price_choice,}
    return render(request,'pages/index.html',context)

def about(request):
    realtor=Realtor.objects.order_by('-hire_date')
    mvp_realtor=Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtor,
        'mvp_realtors':mvp_realtor
    }

    return render(request,'pages/about.html',context)
