from django.db import models
from django.utils import timezone


class Category_type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    date_created = models.DateField(default=timezone.now)
    describe = models.TextField(blank=True)
    category = models.ForeignKey(Category_type, on_delete=models.DO_NOTHING)
    visible = models.BooleanField(default=True)
    photo = models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')

    def __str__(self):
        return self.first_name
