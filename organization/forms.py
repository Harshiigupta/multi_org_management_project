from django import forms
from .models import Organization, CustomUser, Role

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'is_main']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'organization', 'role']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']