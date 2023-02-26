from .models import TeacherDetails
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherDetails
        fields = ['First_Name','Last_Name','Profile_picture','Email_Address','Phone_Number','Room_Number','Subjects_taught']
       
            
        
            
        
        
        
        
        
          