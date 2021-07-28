from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
# Create your models here.

class Task(models.Model):
    """
    [summary]

    """
    # class Meta:
    #     ordering = ["deadline"]

   
    PIORITY_CHOICES = [('H','High'),('M','Medium'),('L','Low')]
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Categories',on_delete=models.CASCADE,null=True)
    piority = models.CharField(max_length=1,choices=PIORITY_CHOICES,default='L')
    deadline = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    def rest_time(self):
        residual_time =self.deadline -datetime.date.today()
        return residual_time
    

class Categories(models.Model):
    class Meta:
        ordering = ["task_group"]

    task_group = models.CharField(max_length=50)

    def __str__(self):
        return self.task_group