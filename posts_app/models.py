from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    create_at =models.DateTimeField(auto_now_add=True)#adiciona automaticamente

    def __str__(self): #recebendo o titulo para que fique visivel no blog
        return self.title