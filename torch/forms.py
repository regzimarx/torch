from django import forms
from .models import StudentRecord

class StudentRecordForm(forms.ModelForm):
    """ model form for student records
    """
    
    def __init__(self, *args, **kwargs):
        super(StudentRecordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = StudentRecord
        fields = '__all__'