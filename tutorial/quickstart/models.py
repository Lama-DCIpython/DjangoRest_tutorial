from django.db import models

# Create your models here.


class Book(models.Model):
    objects = None
    name = models.CharField(max_length=50, null=True)
    pub_date = models.DateField()

    class Meta:
        ordering = ['pub_date']

