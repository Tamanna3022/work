from . import views
from django.urls import path, include
from rest_framework import routers # responsible for generating all the urls for particular model

routers = routers.DefaultRouter()
routers.register('languages', views.LanguageView)
routers.register('paradigms', views.ParadigmView)
routers.register('programmers', views.ProgrammerView)


urlpatterns = [
    #path('', include('languages.urls'))
    path('', include(routers.urls))
    
]
  
'''here we have setted up the router regiterations and the linkings of our different models with views and path'''