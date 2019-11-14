from django.db import models

class Schedule (models.Model):  
    start = models.IntegerField()
    end = models.IntegerField()

class Movie (models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField() 
    duration=models.FloatField(max_length=100) 
    def __str__(self):
        return self.name 

class Room (models.Model):  
    name = models.CharField(max_length=50)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
    
class Session (models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    schedule=models.ForeignKey(Schedule, on_delete=models.CASCADE)
    def __str__(self):
        return self.movie.name 

class Client(models.Model):  
    name= models.CharField(max_length=50)
    age= models.IntegerField()
    session=models.ManyToManyField(Session)
    def __str__(self):
        return self.name
# Create your models here.
