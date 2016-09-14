import random
from django.core.management.base import BaseCommand
from faker import Faker
from books.models import Author, Book


fake = Faker()


class Command(BaseCommand):
    help = 'Add fake books data'

    def handle(self, *args, **kwargs):
        for _ in range(100):
            self._generate_authors()

    def _generate_authors(self):
        author_name = fake.name()
        author = Author(name=author_name)
        author.save()
        self._generate_books(author)

    def _generate_books(self, author):
        for _ in range(random.randrange(5, 20)):
            title = self._generate_book_title()
            book = Book(
                title=title,
                author=author
            )
            book.save()

    def _generate_book_title(self):
        return " ".join(
            fake.text().split()[0:random.randrange(2, 5)]
        )
