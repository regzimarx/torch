from django.conf.urls import url, include
from django.contrib import admin
import views

from .views import (
    HomeView,
    SubmissionsView,
    SubmissionsFormView,
    SubmissionsSuccessView,
    RecordsView,
    SingleRecordView,
    RecordUpdate
)

urlpatterns = [
    # url(r'^admin/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^submissions/$', SubmissionsView.as_view(), name='submissions'),
    url(r'^submissions/form/$', SubmissionsFormView.as_view(), name='submissions_form'),
    url(r'^submissions/success/$', SubmissionsSuccessView.as_view(), name='submissions_success'),
    url(r'^ajax/departments/', views.get_courses, name='get_courses'),
    url(r'^staff/records/$', RecordsView.as_view(), name='records'),
    url(r'^staff/record/(?P<id>[0-9]+)/$', SingleRecordView.as_view(), name='single-record'),
    url(r'^staff/record/(?P<id>[0-9]+)/edit/$', RecordUpdate.as_view(), name='update-record')
]
