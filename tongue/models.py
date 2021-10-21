from django.db import models

# Create your models here.
class participant(models.Model):
    p_name=models.CharField(max_length=100)
    time=models.TimeField()
