from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 10000)
    date = models.DateField(auto_now_add = True)
    time = models.TimeField(auto_now_add = True)