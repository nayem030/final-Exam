from django.contrib import admin
from . import models

class ItemAdmin(admin.ModelAdmin):
    list_display=('title','description',)
    prepopulated_fields={'slug':('title',)}

admin.site.register(models.Item, ItemAdmin)