from django.contrib import admin
from .models import *

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'city', 'region']
    list_filter = ['city', 'region', 'tags']

class HotelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'city', 'region']
    list_filter = ['city', 'region', 'work_days','tags']

class PlaceReviewAdmin(admin.ModelAdmin):
    list_display = ['place']
    list_filter = ['place', 'rating']

class HotelReviewAdmin(admin.ModelAdmin):
    list_display = ['hotel']
    list_filter = ['hotel', 'rating']

admin.site.register(Place, PlaceAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(PlaceReview, PlaceReviewAdmin)
admin.site.register(HotelReview, HotelReviewAdmin)
admin.site.register(WorkDay)
admin.site.register(Tag)
admin.site.register(Faq)
admin.site.register(Social)
admin.site.register(Contact)
admin.site.register(Attachment)
admin.site.register(City)
admin.site.register(Region)