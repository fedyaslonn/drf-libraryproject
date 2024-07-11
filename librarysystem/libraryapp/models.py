from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    publication_date = models.DateField(default=timezone.now)

