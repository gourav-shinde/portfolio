from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from .serializer import FeedbackSerializer
# Create your views here.

def homePage(request):
    return render(request,"index.html",{})



@api_view(['POST',])
def getfeedback(request):
    if request.method=="POST":
        serializer=FeedbackSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

