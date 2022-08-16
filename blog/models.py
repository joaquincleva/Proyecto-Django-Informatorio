from django.db import models
from acoounts.models import User

class Post(models.Model):
    titulo = models.CharField("Titulo", max_length=200)
# Create your models here.
class Comment(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    cuerpo = models.TextField("Cuerpo")