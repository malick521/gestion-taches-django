from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=150)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    

