from django.db import models

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    type = models.CharField(max_length=200) #Stock or MRO
    created = models.DateField(auto_now_add=True)
    price = models.DateField(null=True)
    cost = models.DateField(null=True)
    date_ingoing = models.DateField(null=True, blank=True)
    date_outgoing = models.DateField(null=True, blank=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.t + ' - by ' + self.user.username

class Trabajador(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.CharField(max_length=50)