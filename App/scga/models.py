from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EstacaoTrabalho(models.Model):
    identificador=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=20)
    modelo=models.CharField(max_length=12)
    serial=models.CharField(max_length=20)
    setor=models.CharField(max_length=10)
    
    
class Impressoras(models.Model):
    ident=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=20)
    modelo=models.CharField(max_length=12)
    cupsid=models.CharField(max_length=20)
    setor=models.CharField(max_length=10)


class Telefones(models.Model):
    identel=models.AutoField(primary_key=True)
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=12)
    ramal=models.CharField(max_length=20)
    setor=models.CharField(max_length=10)
    
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)