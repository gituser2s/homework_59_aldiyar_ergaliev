from django.contrib import admin
from webapp.models import Task, Type, Status

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'detailed_description', 'status', 'created_at')
    list_filter = ('id', 'description', 'detailed_description', 'status', 'type', 'created_at')
    search_fields = ('description', 'detailed_description', 'status', 'type',)
    fields = ('description', 'detailed_description', 'status', 'type', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')


admin.site.register(Task, TaskAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('title',)
    fields = ('title',)
    readonly_fields = ('id',)


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('title',)
    fields = ('title',)
    readonly_fields = ('id',)


admin.site.register(Status, StatusAdmin)
