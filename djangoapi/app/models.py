from django.db import models

class App(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name

