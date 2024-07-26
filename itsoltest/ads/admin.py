from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'ad_id', 'author', 'views', 'position')
    search_fields = ('title', 'author')
    list_filter = ('author',)
