from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    number_of_pages = models.IntegerField()
    ImagePath = models.CharField(max_length=500, null=True)
    sales_number = models.IntegerField(default=0)
    description = models.TextField()

    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()


class BookCategory(models.Model):
    name = models.CharField(max_length=50)
