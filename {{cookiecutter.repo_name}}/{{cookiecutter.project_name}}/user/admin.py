from django.contrib import admin

from user.models import Account

class AccountAdmin(admin.ModelAdmin):
    """
        Account Model admin with display liast,link,read only feilds and search option.
    """
    icon = '<i class="material-icons">account_circle</i>'
    list_display = ['id', 'is_active', 'mobile', 'email', 'uuid']


admin.site.register(Account, AccountAdmin)
