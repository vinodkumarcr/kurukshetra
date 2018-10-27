from django.db import models

class registration(models.Model):
    genders=(('f','Female'),('m','Male'))
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Username=models.CharField(max_length=100,unique=True)
    PhoneNo=models.IntegerField()
    Email_Id=models.EmailField()
    password=models.CharField(max_length=20)
    Your_Birth=models.DateField()
    Gender=models.CharField(max_length=1,choices=genders)

    def __str__(self):
        return self.Username

class sandesh_send(models.Model):
    datetime=models.DateTimeField(auto_now_add=True)
    sandesh=models.CharField(max_length=500)

    def __str__(self):
        return self.sandesh[0:20]
