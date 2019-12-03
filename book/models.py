from django.db import models
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    isbn  = models.CharField(max_length=13, unique = True, primary_key = True)
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, null=True)
    published = models.CharField(max_length=20,null=True)
    page = models.CharField(max_length=10, null=True)
    price = models.CharField(max_length=10, null=True)
    book_logo = models.TextField(null=True)
    description = models.TextField(null=True)
    callnumber = models.CharField(max_length=100)
    createtime = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Book'

class College(models.Model):
    name = models.CharField(max_length=100)
    college_description = models.TextField(null = True)
    class Meta:
        db_table = 'College'

class Author(models.Model):
    name = models.CharField(max_length=100)
    author_description = models.TextField(null = True)
    author_logo = models.TextField(null=True)
    college = models.ForeignKey(College, on_delete='CASCADE')
    class Meta:
        db_table = 'Author'

class AuthorBook(models.Model):
    book = models.ForeignKey(Book, on_delete='CASCADE')
    author = models.ForeignKey(Author, on_delete='CASCADE')
    class Meta:
        db_table = 'AuthorBook'



