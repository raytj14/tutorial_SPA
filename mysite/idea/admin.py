from django.contrib import admin

from .models import Idea

class IdeaModelAdmin(admin.ModelAdmin):
    list_display = ('idea', 'remind', 'status', 'created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(Idea, IdeaModelAdmin)
