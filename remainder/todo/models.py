from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
# Create your models here.


class ExpiredTaskManager(models.Manager):

    def set_expired(self):
        return self.filter(deadline__lt=timezone.now())

class EmptycategoriesManager(models.Manager):
    
    def empty_categories(self):
        return self.filter(category__isnull=True)

class Task(models.Model):
   
    PIORITY_CHOICES = [('High','High'),('Medium','Medium'),('Low','Low')]
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=100)
    created_date = models.DateTimeField(default=datetime.date.today)
    category = models.ForeignKey('Categories',on_delete=models.CASCADE,null=True)
    piority = models.CharField(max_length=10,choices=PIORITY_CHOICES,default='Low')
    deadline = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    objects = ExpiredTaskManager()

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    def set_status(self):
        "Returns whether the Tasks's due date has passed or not."
        if self.deadline and datetime.date.today() > self.deadline:
            self.status = True
            self.save()

class Categories(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=50)
    objects = EmptycategoriesManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories_detail', args=[str(self.id)])

