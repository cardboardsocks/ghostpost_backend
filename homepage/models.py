from django.db import models
from django.utils import timezone
# Create your models here.

class Roast_Boast(models.Model):
    is_boast = models.BooleanField()
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.content