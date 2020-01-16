from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=256,unique=True)
    grade = models.IntegerField(default=11)
    subject = models.CharField(max_length=128, default='Both')
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.title



