from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # vincular Perfil con la clase de Django User
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=50, default="Chile")


    def __str__(self):
        return f'Este es el perfil del usuario {self.usuario.username}'

