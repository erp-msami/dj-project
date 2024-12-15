# from django.contrib import admin
# from .models import Course
# Register your models here.
# admin.site.register(Course)

from django.contrib import admin
from .models import Course, Lesson, Enrollment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)