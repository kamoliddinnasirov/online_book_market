from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Input genre book', verbose_name='Book name')



    def __str__(self) -> str:
        return self.name 
    

class Language(models.Model):
    name = models.CharField(max_length=200, help_text='Input language book', verbose_name='Book language')



    def __str__(self) -> str:
        return self.name 
    


class Publisher(models.Model):
    name = models.CharField(max_length=200, help_text='Input publisher book', verbose_name='Book publisher')



    def __str__(self) -> str:
        return self.name 
    
    

class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text='Input first name', verbose_name="first name")
    last_name = models.CharField(max_length=100, help_text='Input last name', verbose_name="last name")
    date_of_birth = models.DateField(
        help_text='Input date of birth', 
        verbose_name="date of birth",
        null=True, blank=True
        )
    about = models.TextField(help_text="Input about author", verbose_name='about')
    photo = models.ImageField(upload_to='Author/%Y/%m/%d', help_text='Input author photo', verbose_name='photo')




    def __str__(self) -> str:
        return self.last_name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    language = models.ForeignKey("Language", on_delete=models.RESTRICT)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    author = models.ManyToManyField("Author")
    summary = models.TextField(max_length=100)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    photo = models.ImageField(upload_to='Book/%Y/%m/%d')


    def __str__(self) -> str:
        return self.title 
    

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])



