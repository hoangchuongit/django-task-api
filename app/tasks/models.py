from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
