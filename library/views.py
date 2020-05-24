from django.shortcuts import render,get_object_or_404,redirect

from .models import Books,BooksRead
from django.db.models import Q,QuerySet
from django.http import HttpResponseNotFound


def library_view(request):
    books = Books.objects.filter(empty=False)
    query = request.GET.get('q')
    if query:

        books = books.filter(Q(name__icontains=query)).distinct()
    else:
        query = None
    context = {
        'books':books,
        'title':'Books',
        'query':query,
    }

    return render(request,'library-books-list.html',context)

def borrowed_books_view(request):
    books = BooksRead.objects.all()

    query = request.GET.get('q')
    if query:

        books = books.filter(Q(book__name__icontains=query)).distinct()
    else:
        query = None

    context = {
        'books':books,
        'title':'Borrowed Books',
        'query':query,
    }

    return render(request,'borrowed-books-view.html',context)



def books_read_view(request,book_id):
    if request.user.is_authenticated:

        book = get_object_or_404(Books,id=book_id,empty=False)
        if BooksRead.objects.filter(user=request.user,book=book):
            return redirect('books')

        BooksRead.objects.create(user=request.user,book=book)
        book.empty = True
        book.save()

        return redirect('books')
    else:
        return HttpResponseNotFound('404')

def books_read_return_view(request,book_id):
    if request.user.is_authenticated:

        book = get_object_or_404(Books,id=book_id,empty=True)
        booksread = get_object_or_404(BooksRead,book=book)
        booksread.delete()
        book.empty = False
        book.save()

        return redirect('my-books')
    else:
        return HttpResponseNotFound('404')