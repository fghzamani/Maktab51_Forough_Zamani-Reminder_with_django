from django.shortcuts import render
from django.views.generic import ListView , DetailView,CreateView,UpdateView , DeleteView
from .models import Task ,Categories
from django.urls import reverse_lazy 
import datetime


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    
    def get_context_data(self,**kwargs):
        context = super(TaskListView,self).get_context_data(**kwargs)
        context['expired_list'] = Task.objects.set_expired()
        print(context)
        return context

    
class TaskDetailView(DetailView): 
    model = Task
    template_name = 'task_detail.html'

class TaskCreateView(CreateView): 
    model = Task
    template_name = 'task_new.html'
    fields = ('title', 'body','category','piority','deadline','status')
  

class TaskUpdateView(UpdateView):
    model = Task
    fields = ('title', 'body','deadline','category','status')
    template_name = 'task_edit.html'

class TaskDeleteView(DeleteView): 
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')

class CategoriesView(ListView):
    model = Categories
    template_name = 'categories_list.html'


class DetailsCategoriesView(DetailView):
    context_object_name = 'categories_detail'
    model = Categories
    template_name = 'categories_detail.html'
    def get_context_data(self,**kwargs):
        context = super(DetailsCategoriesView,self).get_context_data(**kwargs)
        context['cat_list'] = Categories.objects.all()
        print(context)
        return context 

class EmptyCategoriesViews(ListView):
    model = Categories
    template_name = 'categories_list.html'
    
    def get_context_data(self,**kwargs):
        context = super(EmptyCategoriesViews,self).get_context_data(**kwargs)
        context['empty_list'] = Categories.objects.empty_categories()
        print(context)
        return context

   