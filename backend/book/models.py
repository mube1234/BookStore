from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category,null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='files/')
    book_file = models.FileField(upload_to='files/')  

    def __str__(self):
        return self.title
