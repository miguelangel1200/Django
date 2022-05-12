from unicodedata import decimal
from django.db import models

# Create your models here.

class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    activate = models.IntegerField(default=0)
    email = models.EmailField(max_length=250)
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=150)

    def __str__(self):
        return self.role

class user_role(models.Model):
    user_user_id =  models.ForeignKey(users)
    role_role_id = models.ForeignKey(roles)

class courses(models.Model):
    idcourses = models.AutoField(primary_key=True)
    name_course = models.CharField(max_length=250)
    description = models.CharField(max_length=300)
    price_course = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=500)
    users_user_id = models.ForeignKey(users)

    def __str__(self):
        return self.name_course

class assitens(models.Model):
    idassistens = models.AutoField(primary_key=True)
    abstens = models.CharField(max_length=100)
    delay = models.CharField(max_length=100)
    courses_idcourses = models.ForeignKey(courses)

class notes(models.Model):
    idnotes = models.AutoField(primary_key=True)
    note_1 = models.DecimalField(max_digits=4, decimal_places=2)
    note_2 = models.DecimalField(max_digits=4, decimal_places=2)
    note_3 = models.DecimalField(max_digits=4, decimal_places=2)
    note_4 = models.DecimalField(max_digits=4, decimal_places=2)
    note_5 = models.DecimalField(max_digits=4, decimal_places=2)
    average = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.average

class estate(models.Model):
    idestate = models.AutoField(primary_key=True)
    name_estate = models.CharField(max_length=50)
    notes_idnotes = models.ForeignKey(notes)

    def __str__(self):
        return self.name_estate

class certificates(models.Model):
    idcertificate = models.AutoField(primary_key=True)
    name_certificate = models.CharField(max_length=250)
    
    user_user_id =  models.ForeignKey(users)
    courses_idcourses = models.ForeignKey(courses)


