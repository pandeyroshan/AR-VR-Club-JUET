from django.db import models

# Create your models here.

class Messages(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return 'Message from '+self.fname
    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Messages'