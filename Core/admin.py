from django.contrib import admin
from .models import Messages,Profile,Task,GroupAR,TaskStatus,Meetings
# Register your models here.


admin.site.register(Messages)
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(GroupAR)
admin.site.register(TaskStatus)
admin.site.register(Meetings)