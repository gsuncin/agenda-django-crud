from django.db import models
from datetime import datetime


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    main_phone = models.CharField(max_length=11)
    secundary_phone = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='crud_init/images', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def formal_name(self):
        return f'{self.name} {self.surname[0]}'

    def person_age(self):
        return datetime.now().date() - self.birth_date


class Agenda(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person")
