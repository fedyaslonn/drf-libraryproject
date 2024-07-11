from django.urls import path
from .views import BookApi, AuthorApi, LoanApi

urlpatterns = [
    path('books/', BookApi.as_view(), name='book-list'),
    path('books/<int:pk>/', BookApi.as_view(), name='book-detail'),
    path('authors/', AuthorApi.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorApi.as_view(), name='author-detail'),
    path('loans/', LoanApi.as_view(), name='author-list'),
    path('loans/<int:pk>/', LoanApi.as_view(), name='author-detail'),

]