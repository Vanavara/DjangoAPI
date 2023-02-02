from rest_framework import serializers
from .models import App

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'url', 'language', 'price')

#comment for checking gitHub connection