
from django.contrib import admin
from django.urls import path, include
from name import views 
from rest_framework.routers import DefaultRouter

''' what do the viewsets mainly neeeded for:  We don't need to maintain the urls of different views
just make a router and register your class with router and rest work will be done by
viewsets itself
# we need router because we are not making urls for every part differently but the router will automatically make the 
# urls for the viewsets avilable in our views'''

#creating router object
router = DefaultRouter()
# regiter studentviewset with router
router.register('student',views.StudentViewSet, basename='Student')
# we have to mention where our router url is present because till now our program doesnt know where it is
# so we have to make a end point so that router can do it's work

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))  
# this is used to tell the router about the views and the models like where they are present
]
