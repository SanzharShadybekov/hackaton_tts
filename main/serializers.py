from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class TranslateSerializer(serializers.Serializer):
    data = serializers.CharField(required=True, max_length=1000)
