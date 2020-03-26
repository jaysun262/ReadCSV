from django.conf import settings
from django.db import models


class DataStore(models.Model):
    f_name = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=2000, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.email 
