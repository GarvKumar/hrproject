from django.db import models

# Create your models here.
class Notification(models.Model):
    notificationtext=models.CharField(max_length=200)
    notificationdate=models.CharField(max_length=30)