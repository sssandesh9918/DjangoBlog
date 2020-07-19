from django.contrib import admin
from .models import Contents
# Register your models here.
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_at')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Contents, ContentsAdmin)