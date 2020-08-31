from django.shortcuts import render
from django.views import generic
from .models import TodoModel
from django.urls import reverse_lazy

class TodoList(generic.ListView):
  template_name = 'list.html'
  model = TodoModel

class TodoDetail(generic.DetailView):
  template_name = 'detail.html'
  model = TodoModel

class TodoCreate(generic.CreateView):
  template_name = 'create.html'
  model = TodoModel
  fields = ('title', 'memo', 'priority', 'duedate')
  success_url = reverse_lazy('list') 

class TodoDelete(generic.DeleteView):
  template_name = 'delete.html'
  model = TodoModel
  success_url = reverse_lazy('list')

class TodoUpdate(generic.UpdateView):
  template_name = 'update.html'
  model = TodoModel
  fields = ('title', 'memo', 'priority', 'duedate')
  success_url = reverse_lazy('list')


