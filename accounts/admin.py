from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    list_filter = ('email', 'first_name', 'last_name', 'role')
    fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'password')
        }),
        ('Permissions', {'fields':(
            'is_staff', 'is_active', 'groups', 'user_permissions'
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
admin.site.register(CustomUser, CustomUserAdmin)