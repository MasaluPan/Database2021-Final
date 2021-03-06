from django.contrib import admin
from lecture.models import *

# Register your models here

admin.site.register(Department)
admin.site.register(Student_Status)
admin.site.register(Student_Class)
admin.site.register(Student_Grade)

admin.site.register(Selected_Result)
admin.site.register(Feedback_Result)

admin.site.register(Teacher)
admin.site.register(Course_Credit)
admin.site.register(Semester)
admin.site.register(Course_Type)
admin.site.register(Course_Status)

admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Location)
admin.site.register(Course_Time)

admin.site.register(Student)

class Profile_CourseInfo(admin.ModelAdmin):
    list_display = ('course_name', 'semester','course_type', 'teacher',
            'location', 'course_time', 'course_credit', 'course_max_count', 
            'department', 'course_class')

admin.site.register(Course_Info, Profile_CourseInfo)
admin.site.register(Enroll)
