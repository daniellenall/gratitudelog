from django.db import models
from django.contrib.auth.models import User

class Gratitude(models.Model):
    title = models.TextField()
    date = models.DateField(auto_now=True)
    highlight = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="author_gratitude")

    def __str__(self):
        return self.title