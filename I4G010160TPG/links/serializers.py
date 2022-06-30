from .models import Link
from rest_framework import serializers

class LinkSerializer(serializers.ModelSerializer):
    model = Link
    fields = '__all__'
