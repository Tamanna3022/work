from django.db import models


'''the language class will depend upon the paradigm model so we will conect with use of 
forign key
paradigm is the type of what skill we are adding'''

class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
'''models.cascade is used to delete  the row if the forifn key is deleted'''

'''observation: as we have given the foriegn key reference for the paradigm class we can not write a new paragm
here we have to choose from the paradigms already present in the paradigm model
Same will hapeen for the programmer model as we have given a manytomany field it will take the inputs of the lnaguage
model itself'''
class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name





'''this class will represents the programmers
here we are using manytomany field because a single programmer can have one or more language skill
so to pair it with proper paradigm we are using it
'''
class Programmer(models.Model):
    name = models.CharField(max_length=50) 
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
    
'''we had already created the language model and see the functionality on the server port as we were able to add
the languages and paradigm nd we were able to see them through the help of the serializer and the view part using 
url dispathers but now as we know we need more models'''
'''so what we are doing here is making more 2 models paradigm for the language type and programmer for the
manytomny field access and after making it we had  forign key indent for the pardigm class
now our models are set we will go to the serializer.py file'''
    

