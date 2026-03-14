from django.contrib import admin

# Register your models here.

from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")


admin.site.register(Project, ProjectAdmin)



class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "is_completed")


admin.site.register(Task, TaskAdmin)

