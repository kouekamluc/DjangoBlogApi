from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm , CustomUserCreateForm
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form  = CustomUserChangeForm
    model = CustomUser
    
    list_display = ["email", "username","name","is_staff",]
    

admin.site.register(CustomUser , CustomUserAdmin)