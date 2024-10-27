

from rest_framework import serializers
from .models import Client, Project
from .models import Client, Project
from django.contrib.auth.models import User
from django.utils import timezone
import pytz

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    created_by = serializers.SerializerMethodField()  
    created_at = serializers.SerializerMethodField()  

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

    def get_created_by(self, obj):
        
        return obj.created_by.username if obj.created_by else None

    def get_created_at(self, obj):
        
        ist = pytz.timezone('Asia/Kolkata')
        return obj.created_at.astimezone(ist).strftime('%Y-%m-%d %H:%M:%S')

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.SerializerMethodField()  
    created_at = serializers.SerializerMethodField() 

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'projects', 'updated_at']

    def get_created_by(self, obj):
        
        return obj.created_by.username 

    def get_created_at(self, obj):
        
        ist = pytz.timezone('Asia/Kolkata')
        return obj.created_at.astimezone(ist).strftime('%Y-%m-%d %H:%M:%S')
