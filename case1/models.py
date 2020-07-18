from django.db import models


# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    birthdate = models.DateTimeField()
    studentreg_no = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id)


class Info(models.Model):
    id = models.AutoField()
    phonenumber = models.IntegerField(max_length=15)
    email = models.EmailField()
