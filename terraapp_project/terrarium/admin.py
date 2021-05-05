from django.contrib import admin
from .models import Animal, Temperature, Humidité
# Register your models here.
admin.site.register(Animal)
admin.site.register(Temperature)
admin.site.register(Humidité)

