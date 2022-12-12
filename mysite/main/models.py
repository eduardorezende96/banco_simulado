from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MovesList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="moveslist", null=True)
    name = models.CharField(max_length=200)
    totalLista = models.FloatField()
    
    def __str__(self):
        return self.name


class Move(models.Model):
    moveslist = models.ForeignKey(MovesList, on_delete=models.CASCADE)
    data = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)
    value = models.FloatField()
    tipo = models.BooleanField()
    
    def __str__(self):
        return str(self.value)