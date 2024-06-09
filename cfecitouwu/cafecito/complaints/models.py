from django.db import models

class Complaint(models.Model):
    RUT_CHOICES = [
        ('Reclamo', 'Reclamo'),
        ('Felicitaciones', 'Felicitaciones'),
    ]
    
    rut = models.CharField(max_length=12)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateField()
    description = models.CharField(max_length=15, choices=RUT_CHOICES)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.description}"
