from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class calculatorserializer(serializers.ModelSerializer):
    class Meta:
        model = calculatordata
        fields = '__all__'