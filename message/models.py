from django.db import models
class query(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject =models.CharField(max_length=100)
    msg = models.TextField()
    
    def __str__(self):
        return self.name
# Create your models here.
