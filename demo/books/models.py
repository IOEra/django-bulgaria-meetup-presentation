from __future__ import unicode_literals

from django.db import models as m


class Author(m.Model):
    name = m.CharField(max_length=70)


class Book(m.Model):
    title = m.CharField(max_length=128)
    author = m.ForeignKey(Author)
