from django.db import models
from django.utils import timezone
import ast

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=100, verbose_name = '学院名称')
    college_description = models.TextField(blank=True, null = True, verbose_name = '学院简介')
    
    class Meta:
        db_table = 'College'
        verbose_name = '学院表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name = '作者姓名')
    birthday = models.CharField(max_length=100, blank=True, null = True, verbose_name = '出生年月')
    author_description = models.TextField(blank=True, null = True, verbose_name = '作者简介')
    author_logo = models.TextField(blank=True, null=True, verbose_name = '作者图片URL')
    college = models.ForeignKey(College, on_delete=models.CASCADE, verbose_name = '所属学院')

    class Meta:
        db_table = 'Author'
        verbose_name = '作者表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn  = models.CharField(max_length=15, unique = True, verbose_name = 'ISBN')
    title = models.CharField(max_length=100, verbose_name = '图书名称')
    publisher = models.CharField(max_length=100, null=True, blank = True, verbose_name = '出版社')
    published = models.CharField(max_length=100, null=True, blank = True, verbose_name = '出版日期')
    page = models.IntegerField(null=True, blank = True, verbose_name = '页数')
    price = models.CharField(max_length=10, null=True, blank = True, verbose_name = '价格')
    book_logo = models.TextField(null=True, blank=True, verbose_name = '图书图片URL')
    description = models.TextField(null=True, blank=True, verbose_name = '图书简介')
    callnumber = models.CharField(null=True, max_length=100, blank=True, verbose_name = '索书号')
    createtime = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True, verbose_name = '是否公开')
    authors = models.ManyToManyField(Author, through='AuthorBook', verbose_name = '作者')
    #authors = models.ManyToManyField(Author, verbose_name = '作者')

    #获取这本书的所有作者，按照优先级降序输出
    def GetAuthor(self):        
        allauthor = AuthorBook.objects.filter(book__isbn=self.isbn).order_by('-priority')
        ans = ""
        first = 1
        for every in allauthor:
            if first == 1:
                first = 0
            else:
                ans += ", "
            ans += every.author.name
        return ans

    GetAuthor.short_description = '作者'


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Book'
        verbose_name = '图书表'
        verbose_name_plural = verbose_name



class AuthorBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = '图书')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name = '作者')
    priority = models.IntegerField(default=0, verbose_name = '优先级')
    class Meta:
        db_table = 'AuthorBook'
        verbose_name = '图书作者表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book.title+" "+self.author.name
        

class User(models.Model):
    username = models.CharField(max_length=15, unique=True, verbose_name = '用户名')
    password = models.CharField(max_length=15, verbose_name='密码')
    newpassword = models.CharField(max_length=15, verbose_name='新密码', null = True,blank=True)
    class Meta:
        db_table = 'User'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username

