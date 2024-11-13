from django.db import models


COUNTRY_CHOICES = (('EUA', 'USA'), 
                   ('BRA', 'Brazil'), 
                   ('FRANCE', 'France'), 
                   ('ISR', 'Israel'), 
                   ('CHI', 'China'), 
                   ('SKR','South Korea'), 
                   ('ITA','Italy'), 
                   ('CAN','Canada'), 
                   ('AUS','Australia'), 
                   ('UK','UK'),)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField( max_length=100,
                                    choices=COUNTRY_CHOICES)
    
    def __str__(self):
        return self.name
