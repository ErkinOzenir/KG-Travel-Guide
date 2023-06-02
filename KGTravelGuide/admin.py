from django.contrib import admin
from .models import *

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'city', 'region']
    list_filter = ['city', 'region']

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tag)
admin.site.register(Faq)
admin.site.register(Social)
admin.site.register(Contact)
admin.site.register(Attachment)
admin.site.register(City)
admin.site.register(Region)