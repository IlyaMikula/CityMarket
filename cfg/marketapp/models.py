from django.db import models


class Floors(models.Model):
    floors = models.PositiveIntegerField(max_length=3)


class Entrance(models.Model):
    entrance = models.PositiveIntegerField(max_length=3)


class Apartmentnumber(models.Model):
    apartmentnumber = models.CharField(max_length=10)



class Realty(models.Model):
    STATUS = (
        ('sale', 'Sale' ),
        ('buy', 'Buy'),
        ('rent', 'Rent')
    )

    status = models.CharField(max_length=5, choices=STATUS)

    TYPE = (
        ('apartment', 'Apartment'),
        ('house', 'House')
    )

    type = models.CharField(max_length=9, choices=TYPE)

    ROOMS = (
        ('one', 'One'),
        ('two', 'Two'),
        ('three', 'Three'),
        ('four', 'Four'),
        ('five', 'Five or more')
    )

    rooms = models.CharField(max_length=5, choices=ROOMS)
    floors = models.ForeignKey(Floors, on_delete=models.CASCADE)
    entrance = models.ForeignKey(Entrance, on_delete=models.CASCADE)
    apartmentnumber = models.ForeignKey(Apartmentnumber, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    price = models.FloatField(max_length=100)

