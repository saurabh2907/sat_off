from django.db import models

# Create your models here.
class LeaveApplication(models.Model):
    employee_name = models.CharField(max_length=100)
    leave_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    reason_for_leave = models.TextField()