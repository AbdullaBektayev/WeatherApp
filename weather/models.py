from django.db import models

class City(models.Model): # creating database with name City
    name = models.CharField(max_length=30) # coulmn with name (name) and input info CharField with maximum length equal to 30 char

    def __str__(self):
        return self.name
