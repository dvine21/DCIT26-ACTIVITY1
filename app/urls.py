from django.urls import path
from .views import HomePageView, AboutPageView, HobbiesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('hobbies/', HobbiesPageView.as_view(), name='hobbies'),
]