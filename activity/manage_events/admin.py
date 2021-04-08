from django.contrib import admin

# Register your models here.
from .models import Events, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']

    class Meta:
        model = Tag


class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_urgent', 'get_tags']
    search_fields = ['title', 'content']
    list_filter = ['tags', 'author']

    class Meta:
        model = Events


admin.site.register(Events, EventsAdmin)
admin.site.register(Tag, TagAdmin)
