"""
Generated Code Metadata:
========================
Original URL: https://ksp.onsiteapp.co
Prompt: How do I design a user role system (e.g., selecting teams) in a web application, and what database schema could support such a feature efficiently?
Generated: DETERMINISTIC_b1815267df8dbff2
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py - Database models for a role-based team selection system
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return self.username

class Team(models.Model):
    """
    Represents a team that users can belong to.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    """
    Represents a role/permission level within the system.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200, blank=True)
    permissions = models.JSONField(default=dict)  # Stores permission flags
    
    def __str__(self):
        return self.name

class UserTeamRole(models.Model):
    """
    Junction table linking users to teams with specific roles.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('user', 'team')
    
    def clean(self):
        # Prevent duplicate active memberships
        if UserTeamRole.objects.filter(
            user=self.user, 
            team=self.team, 
            is_active=True
        ).exclude(pk=self.pk).exists():
            raise ValidationError('User is already an active member of this team')
    
    def __str__(self):
        return f"{self.user} in {self.team} as {self.role}"

# permissions.py - Custom permission checks
from rest_framework.permissions import BasePermission

class IsTeamAdmin(BasePermission):
    """
    Allows access only to users with admin role in the team.
    """
    def has_permission(self, request, view):
        team_id = view.kwargs.get('team_id')
        if not team_id:
            return False
            
        return UserTeamRole.objects.filter(
            user=request.user,
            team_id=team_id,
            role__name='Admin',
            is_active=True
        ).exists()

class HasTeamPermission(BasePermission):
    """
    Checks if user has specific permission in the team context.
    """
    def __init__(self, permission_name):
        self.permission_name = permission_name
        
    def has_permission(self, request, view):
        team_id = view.kwargs.get('team_id')
        if not team_id:
            return False
            
        return UserTeamRole.objects.filter(
            user=request.user,
            team_id=team_id,
            role__permissions__has_key=self.permission_name,
            is_active=True
        ).exists()

# serializers.py - API serializers
from rest_framework import serializers
from .models import Team, Role, UserTeamRole

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'permissions']

class UserTeamRoleSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    role = RoleSerializer(read_only=True)
    
    class Meta:
        model = UserTeamRole
        fields = ['id', 'user', 'team', 'role', 'joined_at', 'is_active']

# views.py - API endpoints
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Team, Role, UserTeamRole
from .serializers import TeamSerializer, RoleSerializer, UserTeamRoleSerializer
from .permissions import IsTeamAdmin, HasTeamPermission

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    @action(detail=True, methods=['post'], permission_classes=[IsTeamAdmin])
    def add_member(self, request, pk=None):
        team = self.get_object()
        serializer = UserTeamRoleSerializer(data={
            'user': request.data.get('user_id'),
            'team': team.id,
            'role': request.data.get('role_id')
        })
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        team = self.get_object()
        members = UserTeamRole.objects.filter(team=team, is_active=True)
        serializer = UserTeamRoleSerializer(members, many=True)
        return Response(serializer.data)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [HasTeamPermission('manage_roles')]

class UserTeamRoleViewSet(viewsets.ModelViewSet):
    queryset = UserTeamRole.objects.all()
    serializer_class = UserTeamRoleSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [HasTeamPermission('manage_members')]
        return super().get_permissions()

# urls.py - URL routing
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, RoleViewSet, UserTeamRoleViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'memberships', UserTeamRoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Initial data migration (0002_initial_roles.py)
from django.db import migrations

def create_initial_roles(apps, schema_editor):
    Role = apps.get_model('teams', 'Role')
    
    Role.objects.create(
        name='Admin',
        description='Team administrator with full permissions',
        permissions={
            'manage_members': True,
            'manage_roles': True,
            'edit_team': True
        }
    )
    
    Role.objects.create(
        name='Member',
        description='Regular team member',
        permissions={
            'view_team': True,
            'create_content': True
        }
    )

class Migration(migrations.Migration):
    dependencies = [
        ('teams', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(create_initial_roles),
    ]
```
