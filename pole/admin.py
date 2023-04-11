from django.contrib import admin
from pole.models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','t_id','t_name','t_email')

admin.site.register(Teacher,TeacherAdmin)
