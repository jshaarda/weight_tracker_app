from django.db import models
import datetime

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
class Entry(models.Model):
    date = models.DateField(default=datetime.date.today)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    name = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.date

    class Meta:
        ordering = ['date']