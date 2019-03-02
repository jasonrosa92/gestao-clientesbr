from django.db import models

class Person(models.Model):
    primeiro_nome = models.CharField(max_length= 30)
    ultimo_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=5)
    bio = models.TextField()
    foto = models.ImageField(upload_to="clientes_photos", null=True, blank=True)

    def __str__(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome
