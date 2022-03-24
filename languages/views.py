from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

# Create your views here.
#queryset : how do i get the information from database
# ModelViewSet : what is happening what to do when pot, get, delete and so on commands are cliekced basically the standard operations
# serializer_clas : it is the language serializer we had just created
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

''' now as models and serializers are setted up we have to make views for the proper viewable part of the
data from database so we will make views of each model we have created and their queryset and the serializer class
now we will go to the urls.py for the url path linkings'''