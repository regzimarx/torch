from django.contrib import admin
from .models import Department, Course, StudentRecord

from import_export.admin import ImportExportModelAdmin

class StudentRecordAdmin(ImportExportModelAdmin):
    """ Admin for student records
    """
    model = StudentRecord
    list_display = ('last_name', 'first_name', 'department', 'course', 'accepted', )
    list_filter = ('department', 'course', 'accepted', )


class DepartmentAdmin(ImportExportModelAdmin):
    """ Admin for department
    """
    model = Department
    

class CourseAdmin(ImportExportModelAdmin):
    """ Admin for course
    """
    model = Course
    
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(StudentRecord, StudentRecordAdmin)
