from django.db import models
from djmoney.models.fields import MoneyField

product_status = [
    (1, 'Disponible'),
    (2, 'Agotado')
]

binding_type = [
    (1, 'Tapa dura'),
    (2, 'Tapa blanda'),
    (3, 'Grapado'),
    (4, 'Wire')
]

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    availability = models.IntegerField(null=False, blank=False, choices=product_status)
    synopsis = models.TextField(blank=False)
    publisher = models.CharField(max_length=200)
    price = MoneyField(max_digits=9, decimal_places=2, default_currency='ARG')
    isbn = models.BigIntegerField(null=True)
    pages = models.IntegerField(null=True)
    language = models.CharField(max_length=200)
    binding = models.IntegerField(null=False, blank=False, choices=binding_type)
    clasification = models.CharField(max_length=200)
    publication_date = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.quantity

""" class Trabajador(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.CharField(max_length=50) """