from django.db import models
from django.contrib.auth.models import User

class Gratitude(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    highlight = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete = models.CASCADE,)