from django.db import models
# import datetime
# from django.utils import timezone


class Product(models.Model):
    class_choices = (
        ('cream', 'Cream'),
        ('hair', 'Hair'),
        ('body', 'Body'),
        ('face', 'Face'),
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    product_class = models.CharField(max_length=60, choices=class_choices)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    entry_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        # return self.name
        return '{}{}{}{}'.format(self.name, self.product_class, self.price, self.entry_date.ctime())

    

