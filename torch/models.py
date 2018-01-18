from django.db import models


class Department(models.Model):
    """ class for departments
    """
    
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return '{}'.format(self.name)
    
class Course(models.Model):
    """ class for courses
    """
    
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    department = models.ForeignKey('Department')
    
    def __str__(self):
        return '{}'.format(self.name)

class StudentRecord(models.Model):
    """ class for student record
    """
    
    # Basic information
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    
    # Parents information
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    
    # Course information
    department = models.ForeignKey('Department')
    course = models.ForeignKey('Course', blank=True, null=True)
    
    # Other information
    affiliations = models.TextField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    scholarships = models.TextField(blank=True, null=True)
    eligibility = models.CharField(max_length=250, blank=True, null=True)
    
    reference_num = models.CharField(max_length=100, blank=True, null=True)
    casual_num = models.CharField(max_length=100, blank=True, null=True)
    toga_num = models.CharField(max_length=100, blank=True, null=True)
    
    accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
    