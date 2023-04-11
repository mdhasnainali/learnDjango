from django.db import models

# Create your models here.
class Teacher(models.Model):
    t_id = models.IntegerField()
    t_name = models.CharField(max_length=40)
    t_email = models.EmailField(max_length=30)

    def __str__(self):
        return self.t_name