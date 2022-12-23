from django.db import models
from account.models import CustomUSer


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.TextField()
    date_birth = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='authors')

    def __str__(self):
        return self.last_name


class Genre(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    CHOICES = (
        ('in stock', 'In stock'),
        ('out of stock', 'Out of stock')
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    status = models.CharField(CHOICES, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField(Genre)
    owner = models.ForeignKey(CustomUSer, on_delete=models.CASCADE, related_name='books')
    like = models.ManyToManyField(CustomUSer, related_name='likes')

    def __str__(self):
        return self.title
