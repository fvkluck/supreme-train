from django.db import models

# Create your models here.
class ModelA(models.Model):
    some_field = models.IntegerField()

class ModelB(models.Model):
    some_other_field = models.IntegerField()
    model_a = models.ForeignKey(ModelA, on_delete=models.CASCADE)
