from django.contrib import admin
from .models import Organization, Role, CustomUser
admin.site.register(Organization)
admin.site.register(Role)
admin.site.register(CustomUser)