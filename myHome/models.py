from django.db import models

# Create your models here.

class place(models.Model):
    index = models.IntegerField()
    수산물표준코드명 = models.TextField()
    산지조합명 = models.TextField()
