from django.contrib import admin

# Register your models here.
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'login')
    list_display_links = ('nickname', 'login')
    search_fields = ('nickname', 'login',)


admin.site.register(Person, PersonAdmin)