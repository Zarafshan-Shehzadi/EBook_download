from django.db import models

class New_Arrivals(models.Model):
    id = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=20)  # Field name made lowercase.
    author_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, blank=True, null=True)
    book_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to="ebook_shop/images")
    type= models.CharField(max_length=30, blank=True, null=True)
    pdf = models.FileField(upload_to="ebook_shop/files")
   

    def __str__(self):
        return self.book_name








    




