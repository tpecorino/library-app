from django.shortcuts import render

user_books = [
    {
        "slug": "the-little-prince",
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "Genre": "Fantasy"
    },
    {
        "slug": "frankenstein",
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "Genre": "Horror"
    }
]


def get_book_title(book):
    return book['title']


# Create your views here.

def index(request):
    return render(request, 'books/index.html')


def books(request):
    sorted_books = sorted(user_books, key=get_book_title)
    return render(request, 'books/books.html', {
        "user_books": sorted_books
    })


def book_detail(request, slug):
    identified_book = next(book for book in user_books if book["slug"] == slug)
    return render(request, 'books/includes/book.html', {
        "book": identified_book
    })
