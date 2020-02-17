from django.db import models

class Users(models.Model):
    uid = models.CharField(max_length=255)
    nm_user = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nm_user