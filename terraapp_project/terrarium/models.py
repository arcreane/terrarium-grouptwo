from django.db import models



class Temperature(models.Model):

    name = models.CharField(max_length=200, null=True)
    valeur = models.FloatField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)





class Humidité(models.Model):
    name = models.CharField(max_length=200)
    valeur = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=200)
    temperature = models.ForeignKey(Temperature, null=True, on_delete=models.SET_NULL)
    humidite = models.ForeignKey(Humidité, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name
