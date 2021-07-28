from django.shortcuts import render
from django.views.generic import ListView , DetailView,CreateView,UpdateView , DeleteView
from .models import Task
from django.urls import reverse_lazy 
import datetime
# Create your views here.



class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskDetailView(DetailView): 
    model = Task
    template_name = 'task_detail.html'

class TaskCreateView(CreateView): 
    model = Task
    template_name = 'task_new.html'
    fields = ('title', 'body','category','piority','deadline')
  

class TaskUpdateView(UpdateView):
    model = Task
    fields = ('title', 'body','deadline','category')
    template_name = 'task_edit.html'

class TaskDeleteView(DeleteView): 
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')

class CategoriesView(ListView):
    model = Task
    template_name = 'categories.html'
