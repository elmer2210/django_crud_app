from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import BookForm

# Create your views here.


def start(request):
    return render(request, 'pages/home.html')


def we(request):
    return render(request, 'pages/nosotros.html')


def books(request):
    list = Book.objects.all()
    return render(request, 'books/index.html', {'books': list})


def create_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/create.html', {'form': form})


def edit_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('books')
    return render(request, 'books/edit.html', {'form': form})


def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')