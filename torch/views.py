import random
import string

from django.views.generic import TemplateView
from .forms import StudentRecordForm
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.views.generic.edit import UpdateView
from .models import Department

from .models import StudentRecord

from .models import Course


class HomeView(TemplateView):
    template_name = 'home.html'
    

class SubmissionsView(TemplateView):
    template_name = 'submissions.html'
    
class SubmissionsFormView(TemplateView):
    template_name = 'submissions-form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['form'] = StudentRecordForm()
        return kwargs
        
    def post(self, request):
        form = StudentRecordForm(request.POST)
        import pdb; pdb.set_trace()
        if form.is_valid():
            obj = form.save()
            
            reference_code = self.generate_reference_code()
            obj.reference_num = reference_code
            obj.save()
        
        form = StudentRecordForm()
        data = {'obj': obj, 'reference_code': reference_code}
        
        return render_to_response('submissions-success.html', data)
        
    def generate_reference_code(self):
        # Generate random reference code
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
        

class SubmissionsSuccessView(TemplateView):
    """ View for success submission
    """
    template_name = 'submissions_success.html'
    
class RecordsView(TemplateView):
    """ View for records
    """
    template_name = 'records.html'
    
    def get_context_data(self, **kwargs):
        kwargs['students_list'] = StudentRecord.objects.all()
        return kwargs
        
class SingleRecordView(TemplateView):
    """ View for single records
    """
    template_name = 'single-record.html'
    
    def get_context_data(self, **kwargs):
        context = super(SingleRecordView, self).get_context_data(**kwargs)
        context['record'] = StudentRecord.objects.get(pk=kwargs['id'])
        return context
        
        
class RecordUpdate(UpdateView):
    """ View for updating record
    """
    model = StudentRecord
    pk_url_kwarg = 'id'
    fields = '__all__'
    template_name = 'record-update.html'
    
        
        
    
        
def get_courses(request):
    """ Change courses according to selected department
    """
    
    department = request.GET.get('department')
    
    courses =  Course.objects.filter(department__id=department)
    data = list(courses.values())
    data = {'courses':data}
    
    return JsonResponse(data)