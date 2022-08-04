from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class empdetails(models.Model):
    empname=models.CharField(max_length=50)
    empcontact=models.BigIntegerField()
    deptemail=models.EmailField(max_length=50)
