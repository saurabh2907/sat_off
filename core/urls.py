# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('leave_applications', views.leave_applications, name='leave applications'),
    path('remove_entry', views.remove_entry, name='remove_entry'),
    path('export', views.export_to_excel, name='export_to_excel'),
]
