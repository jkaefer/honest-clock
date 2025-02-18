from django.db import models


class Times(models.Model):
    username = models.CharField(max_length=255)
    time_punch = models.CharField(max_length=255)
    site_address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

