"""menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from films.views import *

urlpatterns = [
	path('', main_menu, name = 'main_menu'),
	
    path('films/', one_layer),
    path('cartoons/', one_layer),
    path('series/', one_layer),
    
    path('films/director/', two_layer),
    path('films/year/', two_layer),
    path('films/genre/', two_layer),
    
    path('cartoons/director/', two_layer),
    path('cartoons/year/', two_layer),
    path('cartoons/genre/', two_layer),
    
    path('series/director/', two_layer),
    path('series/year/', two_layer),
    path('series/genre/', two_layer),
    
    path('films/director/davidlynch/', finSel),
    path('films/director/jamescameron/', finSel),
    path('films/director/andrewadamson/', finSel),
    path('films/director/guyritchie/', finSel),
    
    
    path('films/genre/romance/', finSel),
    path('films/genre/comedy/', finSel),
    path('films/genre/action/', finSel),
    path('films/genre/sciencefiction/', finSel),
    path('films/genre/thrill/', finSel),
    path('films/genre/adventure/', finSel),
    path('films/genre/сrime/', finSel),
    
    path('films/year/2005/', finSel),
    path('films/year/2001/', finSel),
    path('films/year/2019/', finSel),
    path('films/year/1984/', finSel),
    path('films/year/1997/', finSel),
    path('films/year/2000/', finSel),
    path('films/year/1986/', finSel),
    path('films/year/2009/', finSel),
    
    path('cartoons/director/andrewadamson/', finSel),
    path('cartoons/director/leeunkrich/', finSel),
    
    path('cartoons/genre/comedy/', finSel),
    path('cartoons/genre/adventure/', finSel),
    
    path('cartoons/year/2001/', finSel),
    path('cartoons/year/2017/', finSel),
    path('cartoons/year/2002/', finSel),
    
    
    path('series/director/davidlynch/', finSel),
    path('series/director/michaeljudge/', finSel),
    
    
    path('series/genre/comedy/', finSel),
    path('series/genre/horror/', finSel),
    
    path('series/year/1990/', finSel),
    path('series/year/2015/', finSel),
]


