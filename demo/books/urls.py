from django.conf.urls import url

from .views import book_index

urlpatterns = [
    url(r'^$', book_index),
]
