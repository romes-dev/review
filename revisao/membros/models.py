from django.db import models

# Create your models here.

class Membro(models.Model):
    nome = models.CharField(max_length=180)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome} com {self.idade} anos."
    

