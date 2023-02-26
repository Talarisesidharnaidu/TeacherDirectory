from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import TeacherDetails
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .serializer import TeacherSerializer
from rest_framework.serializers import Serializer
from rest_framework import serializers
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.permissions import 
# Create your views here.

class TeacherList(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    
    def perform_create(self, serializer):
        queryset = TeacherDetails.objects.all()
        for i in range(len(queryset)):
            l=queryset.values()[i]['Subjects_taught'].split()
            print(l)
            legth = len(l)
            if len(l)>= 5:
                raise serializers.ValidationError({'name': 'Teachers should not select not more than five subjects.'}) 
            break 
        else:
            queryset = TeacherDetails.objects.all()
            
                
                    
        serializer.save()
            
    def get_queryset(self):
        # queryset = TeacherDetails.objects.all()
        # firstname = self.request.query_params.get('First_Name')
        # lastname = self.request.query_params.get('Last_Name')
        # Subjects = self.request.query_params.get('Subjects_taught')
        # if firstname is not None:
        #     queryset = queryset.filter(TeacherDetails__First_Name=firstname)
        # elif lastname is not None:
        #     queryset = queryset.filter(TeacherDetails__Last_Name=lastname)
        # elif Subjects is not None:
        #     queryset = queryset.filter(TeacherDetails__Subjects_taught=Subjects)
            
        # return queryset
        return TeacherDetails.objects.all()
    
class TeachersData(generics.RetrieveUpdateDestroyAPIView):
        queryset = TeacherDetails.objects.all()
        serializer_class = TeacherSerializer 
        filter_backends = [filters.SearchFilter]
    #filterset_fields = ['First_Name', 'Last_Name','Subjects_taught']
        search_fields = ['=First_Name', '=Last_Name','=Subjects_taught']           
                    
         
                
    
    # queryset = TeacherDetails.objects.values('Subjects_taught')
    # #queryset = TeacherDetails.objects.values()
    # querydetails=queryset[0]['Subjects_taught']
    # l=querydetails.split() 
    # if len(l) >=5:
        
    #     print("Teacher need to select 5 subjects only not more than that")
    # else:
    #     print(l)
         
    
        
    #permission_classes = [IsAdminUser]


   
    #permission_classes=[ReviewUserOrReadonly]
   
    
