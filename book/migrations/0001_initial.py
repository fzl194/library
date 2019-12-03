# Generated by Django 2.2.5 on 2019-12-03 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author_description', models.TextField(null=True)),
                ('author_logo', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100, null=True)),
                ('published', models.CharField(max_length=20, null=True)),
                ('page', models.CharField(max_length=10, null=True)),
                ('price', models.CharField(max_length=10, null=True)),
                ('book_logo', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('callnumber', models.CharField(max_length=100)),
                ('createtime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Book',
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('college_description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'College',
            },
        ),
        migrations.CreateModel(
            name='AuthorBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete='CASCADE', to='book.Author')),
                ('book', models.ForeignKey(on_delete='CASCADE', to='book.Book')),
            ],
            options={
                'db_table': 'AuthorBook',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='college',
            field=models.ForeignKey(on_delete='CASCADE', to='book.College'),
        ),
    ]