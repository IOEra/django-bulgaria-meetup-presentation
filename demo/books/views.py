from django.shortcuts import render
from .models import Book


def book_index(request):
    books = Book.objects.select_related("author").all()
    context = {
        "books": books,
    }
    return render(
        request, "books/index.html", context
    )
