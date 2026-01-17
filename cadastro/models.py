from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    criado_em =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class produto(models.Model):
    name = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# Create your models here.
