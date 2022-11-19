from django.contrib import admin

from smartcompost.tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
