from django.urls import path
from .views import library_view,books_read_view,borrowed_books_view,books_read_return_view
urlpatterns = [
    path('books/',library_view,name='books'),
    path('borrowed-books/',borrowed_books_view,name='borrowed-books'),
    
    path('books/read/<book_id>/',books_read_view,name='books-read'),
    path('books/read/return/<book_id>/',books_read_return_view,name='books-read-return'),
]
