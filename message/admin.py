from django.contrib import admin
from.models import query

@admin.register(query)
class messageadmin(admin.ModelAdmin):
    list_display= ['id','name','email','subject','msg']
# Register your models here.
