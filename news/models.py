from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length = 120, blank=True)
    post = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
