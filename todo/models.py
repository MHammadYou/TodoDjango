from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.task[:30]
