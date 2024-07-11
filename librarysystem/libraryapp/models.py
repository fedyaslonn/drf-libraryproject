import datetime
from django.contrib.auth.models import User
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
    publication_year = models.DateField(default=datetime.date.today)


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.pk:
            if (self.return_date - self.loan_date).days < 3:
                raise ValueError("Книга бронируется минимум на 3 дня")
        super(Loan, self).save(*args, **kwargs)