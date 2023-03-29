from django.contrib import admin
from .models import NewUser

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea



class UserAdminConfig(UserAdmin):
    """
    Customize our admin panel
    """

    # right panel to seach and filter
    search_fields = ('username', 'first_name',)
    list_filter = ('username', 'first_name', 'is_admin', 'is_superuser',)

    # main information displayed next to each user
    ordering = ('-start_date',)
    list_display = ('id', 'username', 'first_name', 'is_admin', 'is_superuser')

    # fieldsets manage the display when we click on a specific user
    fieldsets = (
        (None, {'fields': ('username', 'first_name', )}),
        ('Permissions', {'fields': ('is_admin', 'is_superuser',)}),
        ('Personnal', {'fields': ('about',)}),
        )

    # add user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'password1', 'password2', 'is_admin', 'is_superuser')
            }
        ),
    )
admin.site.register(NewUser, UserAdminConfig)