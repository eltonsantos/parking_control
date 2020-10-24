from django.db import models

class Parking(models.Model):
  plate = models.CharField(max_length=150)
  time = models.CharField(max_length=150)
  paid = models.BooleanField(default=False)
  left = models.BooleanField(default=False)

  def __str__(self):
    return self.plate
