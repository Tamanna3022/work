from rest_framework import serializers
from .models import * 
'''modelserializer is the most difficult one for user
# what it do is : it will show us the information that is relevant to our models,
 can also create new models or objects and can also update language for u 
 it is embedded in rest framwork so we don't have to explicitly make it'''



# this serializer is just for the lanuage model
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')


# paradigm serializer
class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url','name')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url','name', 'language')

'''as of now we had learned that serializer helps in doing the things in  effective way there are different serailizers
for different work so we have made threee serializers for one each model with the modelserializer itself
which will provide us the fields and information for all linking the models, now we will got to the views.py
file for setting up the views'''