from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from library.models import BooksRead
from django.db.models import Q,QuerySet
from django.http import HttpResponseNotFound

def my_books_view(request):

    if request.user.is_authenticated:

        books = BooksRead.objects.filter(user=request.user)

        query = request.GET.get('q')
        if query:

            books = books.filter(Q(book__name__icontains=query)).distinct()
        else:
            query = None

        context = {
            'books':books,
            'title':'My Books',
            'query':query,
        }

        return render(request,'user/my-books.html',context)
    else:
        return HttpResponseNotFound('404')
def register_view(request):
        
    if request.user.is_authenticated == False:

        emailError = False
        form = RegisterForm(request.POST or None)

        if form.is_valid():

            user = form.save(commit=False)
            
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user.set_password(password)
            email_data = User.objects.filter(email=email)

            if len(email_data) == 0:

                user.save()
                new_user = authenticate(username=user.username, password=password)
                login(request, new_user)
                return redirect('home')
            else:
                emailError = True
        context = {
            'form':form,
            'title':'Register',
            'emailError':emailError,
        }
        return render(request, "user/register.html",context)
    else:
        return HttpResponseNotFound('404')


def login_view(request):
    if request.user.is_authenticated == False:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        return render(request, "user/login.html", {"form": form,'title':'Login',})
    else:
        return HttpResponseNotFound('404')


def logout_view(request):
    
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return HttpResponseNotFound('404')
