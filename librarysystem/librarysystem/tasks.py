from time import sleep
from django.core.mail import send_mail
from celery import shared_task
@shared_task()
def send_email_task(email_address, book_title):
    send_mail(
        "Бронь книги",
        f"Вы забронировали книгу {book_title}",
        "librarysystemsys@gmail.com",
        [email_address]
    )
