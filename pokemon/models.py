from time import timezone
from django.db import models


class Pokemon (models.Model):
    

    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
    class  PokemonType (models.TextChoices):
        WATER = 'WA', ('WATER')
        GRASS = 'GR', ('GRASS')
        GHOST = 'GH', ('GHOST')
        STEEL = 'ST', ('STEEL')
        FAIRY = 'FA', ('FAIRY')
    type = models.CharField(max_length=2,choices=PokemonType.choices,default=PokemonType.WATER)
    hp           = models.PositiveBigIntegerField()     
    active       = models.BooleanField(default=True)   
    name_fr      = models.CharField(max_length=30,default="")   
    name_ar      = models.CharField(max_length=30,default="")   
    name_jp      = models.CharField(max_length=30,default="")     
    created_at   = models.DateTimeField(auto_created=True)    
    modified_at  = models.DateField(auto_now_add=True)

def __str__(self):
        return self.name
# Create your models here.
