from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),  # Home route
    path('about',views.aboutMe, name='about'),  # About Me route

]