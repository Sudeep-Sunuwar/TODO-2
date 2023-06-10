from django.db import models

# Create your models here.
class TODO (models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    is_completed = models.BooleanField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)


    
