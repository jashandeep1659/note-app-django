from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class NotesList(APIView):  
    permission_classes = [IsAuthenticated]
    def get(self  ,request):
        notes= Note.objects.all().order_by('-created')
        serializer = NoteSerializer(notes , many=True)
        return Response(serializer.data)

    def post(self ,request):
        data = request.data
        data['user'] = request.user.id
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # return Response(serializer.data)
            return Response(serializer.data)