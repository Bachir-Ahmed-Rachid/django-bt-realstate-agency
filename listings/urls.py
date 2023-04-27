from django.urls import path
from . import views
urlpatterns = [
    path("",views.IndexView.as_view(),name="listings"),
    path("<int:pk>",views.ListingView.as_view(),name="listing"),
    path("search",views.search,name="search"),
    
]