from django.db import models

class GridFailure(models.Model):
    failure_type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    severity = models.IntegerField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.failure_type} at {self.location} on {self.timestamp.date()}"