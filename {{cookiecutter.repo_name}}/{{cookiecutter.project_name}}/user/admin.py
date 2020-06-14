from django.contrib import admin

from user.models import MyUser

class MyUserAdmin(admin.ModelAdmin):
    """
        MyUser Model admin with display liast,link,read only feilds and search option.
    """
    icon = '<i class="material-icons">account_circle</i>'
    list_display = ['id', 'is_active', 'mobile', 'email', 'uuid']


admin.site.register(MyUser, MyUserAdmin)
