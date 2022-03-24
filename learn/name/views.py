from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class StudentViewSet(viewsets.ViewSet):  #this will inherit viewset from viewsets in class studentviewset
    # let's look into operations of the viewsets
    #1. list it's action type is get (it will give us all the values)
    def list(self, request):
        print("*********List*********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        stu = Student.objects.all()   #it is a model object
        serializer = StudentSerializers(stu, many = True) #model object got changed into serialized object
        print(serializer.data)
        return Response(serializer.data)   # serialized object changes into json  which is frontend understandable
        
        

    #2. retireive it get us the single object
    def retrieve(self, request, pk = None):
        print("*********Retrieve*********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
    
    def create(self, request):
        print("*********Create*********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'data created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):

        print("*********Update*********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Completed data Update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk):
        print("*********Partial_Update*********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data Update'})
        return Response(serializer.errors)


    def destroy(self, request, pk):
        print("*********Destroy*********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':' Data Deleted'})

            



