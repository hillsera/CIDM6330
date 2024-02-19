from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site"""

    # generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # available books (status = a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # the all() is implied by default
    num_authors = Author.objects.count()

    # Part 5 Challenge yourself prompt - add counts of genres and books with certain word
    num_genres = Genre.objects.filter(name__iexact='true crime').count()
    num_books_the = Book.objects.filter(title__istartswith='The ').count()


    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_the': num_books_the,
    }

    # render html template index.html with data in context var
    return render(request, 'index.html', context=context)