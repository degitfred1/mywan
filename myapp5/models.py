from django.db import models

class rap(models.Model):
      title=models.CharField(max_length=30)
      load=models.FileField(upload_to='media')

