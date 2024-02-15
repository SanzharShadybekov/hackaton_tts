from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.conf import settings
from PIL import Image
from pytesseract import image_to_string
from . import serializers


class ImageUploadView(generics.GenericAPIView):
    serializer_class = serializers.ImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = serializers.ImageSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()
            image = instance.image
            try:
                text = image_to_string(f'{settings.MEDIA_ROOT}/{image}', lang='rus')
                return Response({'obj': serializer.data,
                                 'text': text}, status=200)
            except Exception as e:
                return Response({'msg': f'{e}'}, status=400)
        else:
            return Response(serializer.errors, status=400)







