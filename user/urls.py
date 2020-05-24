from django.urls import path
from .views import my_books_view
urlpatterns = [
    path('my-books/',my_books_view,name='my-books'),
]
