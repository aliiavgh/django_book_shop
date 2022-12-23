from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from django.urls import reverse

from books.models import Book, Genre


def index(request):
    genres = Genre.objects.all()
    return render(request, 'main/index.html', {'genres': genres})


def book_list(request, slug):
    books = Book.objects.filter(genre__slug=slug)
    return render(request, 'main/book_list.html', {'books': books})

def book_like(request, pk):
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    book.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))