from django.db import models
from rest_framework import serializers
from .models import SnipetNotes, Tag, Snipets


class SnipetNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnipetNotes
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SnipetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snipets
        fields = '__all__'
