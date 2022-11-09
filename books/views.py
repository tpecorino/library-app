from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'books/index.html')


def books(request):
    pass


def book_detail(request, book):
    pass
