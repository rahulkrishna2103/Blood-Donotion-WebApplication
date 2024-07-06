from django.db import models

class BloodDonor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.bloodgroup}"

