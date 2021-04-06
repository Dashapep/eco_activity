from django.contrib import admin

# Register your models here.
from .models import Events, Tag

admin.site.register(Events)
admin.site.register(Tag)