from django.contrib import admin
from book.models import College
from book.models import Author
from book.models import Book
from book.models import AuthorBook
from book.models import User

# Register your models here.
admin.site.site_header = "后台管理"
admin.site.site_title = '后台管理'


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    #展示学院表
    list_display = ('id', 'name')
    #点击id和name进入编辑界面
    list_display_links = ('id', 'name')
    #默认按照id升序
    ordering = ('id',)
    #搜索框：搜索名字、学院
    search_fields=['name','college_description']
    #关闭顶部action
    actions_on_top = False
    #开启底部action
    actions_on_bottom=True


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    #展示作者表
    list_display = ('id', 'name', 'birthday','college')
    #点击id和name进入编辑界面
    list_display_links = ('id', 'name')
    #右侧过滤器
    list_filter = ('college',)
    #默认按照id升序
    ordering = ('id',)
    #搜索框：搜索名字、学院
    search_fields=['name','college__name']
    #关闭顶部action
    actions_on_top = False
    #开启底部action
    actions_on_bottom=True

    #raw_id_fields =  ('college',)
    #修改界面修改字段
    fieldsets=(
        (
            "个人基本信息", 
            {
                'fields': ('name','college','birthday')
            }
        ), 
        (
            "详细信息", 
            {
                'fields': ('author_logo','author_description')
            }
        )
    )

    '''def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "college__name":
            kwargs["queryset"] = College.objects.filter(name=request.user)
        return super(AuthorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
'''

@admin.register(AuthorBook)
class AuthorBookAdmin(admin.ModelAdmin):
    #展示图书作者表
    list_display = ('id', 'book','author','priority')
    #点击id和book进入编辑界面
    list_display_links = ('id', 'book')
    #右侧过滤器
    list_filter = ('author__college',)
    #默认按照id升序
    ordering = ('id',)
    #搜索框：搜索名字、学院
    search_fields=['book__title','author__name','author__college__name']
    #关闭顶部action
    actions_on_top = False
    #开启底部action
    actions_on_bottom=True
    
    raw_id_fields =  ('book','author')




class AuthorBookAdminLine(admin.TabularInline):
    model = AuthorBook
    list_display = ('book','author','priority')
    raw_id_fields =  ('book','author')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #展示图书表
    list_display = ('id', 'title', 'isbn', 'GetAuthor','publisher', 'published', 'is_public')
    #点击id和title进入编辑界面
    list_display_links = ('id', 'title')
    #右侧过滤器
    list_filter = ('authors__college',)
    #默认按照id升序
    ordering = ('id',)
    #搜索框：搜索名字、学院
    search_fields=['title','authors__name','authors__college__name']
    #关闭顶部action
    actions_on_top = False
    #开启底部action
    actions_on_bottom=True

    fieldsets=(
        (
            "图书基本信息", 
            {
                'fields': ('title','isbn','publisher','published','page','price','is_public')
                #'filter_horizontal': ('authors' ,)
            }
        ), 
        (
            "详细信息", 
            {
                'fields': ('book_logo','description')
            }
        )
    )
    inlines = [
        AuthorBookAdminLine,
    ]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #展示用户表
    list_display = ('id', 'username')
    #点击id和title进入编辑界面
    list_display_links = ('id', 'username')
    #默认按照id升序
    ordering = ('id',)
    #搜索框：搜索名字、学院
    search_fields=['username']
    #关闭顶部action
    actions_on_top = False
    #开启底部action
    actions_on_bottom=True

    fields = ('username', 'newpassword')
