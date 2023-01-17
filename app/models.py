from django.db import models

# Create your models here.
class Sexo(models.Model):
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.sexo

class EspeciesAnimais(models.Model):
    especie = models.CharField(max_length=100)

    def __str__(self):
        return self.especie

class Animais(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(EspeciesAnimais, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=300)
    idade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

