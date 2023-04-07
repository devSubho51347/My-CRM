from django.db import models


# Create your models here.

class Task(models.Model):
    work_status = [
        ("Dn", "Done"),
        ("Pr", "In Progress"),
        ("Pn", "Pending"),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=2, choices=work_status, blank=False)
    resources = models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return f"{self.title}"
