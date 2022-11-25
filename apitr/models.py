from django.db import models

class Usuario(models.Model):
    USER = 'U'
    CONDUCTOR = 'C'
    ADMIN= 'A'

    USERS_CHOICES = (
        (USER, 'u'),
        (CONDUCTOR, 'c'),
        (ADMIN, 'a'),
    )
    name = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=USERS_CHOICES)

class Comentarios(models.Model):
    comentario = models.CharField(max_length=1000)
    release_date = models.DateField()
    usuario=models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)

class Empresas(models.Model):
    nombre=models.CharField(max_length=100)

class Arduino(models.Model):
    latitud=models.FloatField()
    longitud=models.FloatField()
    
class Vehiculos(models.Model):
    placa=models.CharField(max_length=100)
    arduino=models.ForeignKey(Arduino,null=True,blank=True,on_delete=models.CASCADE)
    empresa=models.ForeignKey(Empresas,null=True,blank=True,on_delete=models.CASCADE)

class Rutas(models.Model):
    ruta=models.CharField(max_length=100)
    empresa=models.ForeignKey(Empresas,null=True,blank=True,on_delete=models.CASCADE)
    arduino=models.ForeignKey(Arduino,null=True,blank=True,on_delete=models.CASCADE)
    vehiculo=models.ForeignKey(Vehiculos,null=True,blank=True,on_delete=models.CASCADE)




