from django.db import models

# Create your models here.

class calculatordata(models.Model):
    value1 = models.IntegerField(default=False)
    value2 = models.IntegerField(default=False)
    operation = models.CharField(max_length=1, default=False)
