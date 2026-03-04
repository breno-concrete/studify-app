from django.urls import path
from . import views
#gerencia urls do site
urlpatterns = [
    path('', views.home_view, name='home'),
    
]