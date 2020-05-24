from django.db import models


class Authors(models.Model):

    full_name = models.CharField(verbose_name='Full name',max_length=200)

    def __str__(self):

        return self.full_name

    class Meta:

        ordering = ['-id']
        verbose_name_plural = 'Authors'




class Books(models.Model):
    
    name = models.CharField(verbose_name='Book name',max_length=200)
    number_of_pages = models.IntegerField(verbose_name="Number of pages",default=1)
    author = models.ForeignKey(Authors,on_delete=models.CASCADE,verbose_name='author')
    image = models.ImageField(verbose_name='Image')
    empty = models.BooleanField(editable=False,default=False)


    def __str__(self):

        return self.name

    class Meta:

        ordering = ['-id']
        verbose_name_plural = 'Books'


class BooksRead(models.Model):

    user = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='User')
    book = models.ForeignKey(Books,on_delete=models.CASCADE,verbose_name='Book')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')


    class Meta:
        ordering = ['-id']
    