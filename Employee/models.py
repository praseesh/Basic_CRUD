from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    age = models.IntegerField()


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "mydatabase_employee"

