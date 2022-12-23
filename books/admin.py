from django.contrib import admin
from books.models import *

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)