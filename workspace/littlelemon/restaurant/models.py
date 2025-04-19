from django.db import models
# models.py
# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {self.price:.2f}'

    def __str__(self):
        return f'{self.title} : {self.price:.2f}'

class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
