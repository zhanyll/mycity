from django.db import models

# Create your models here

class Proposal(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='proposal')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title