from django.urls import path
from .views import TaskListView,TaskDetailView,TaskCreateView ,TaskUpdateView , TaskDeleteView ,CategoriesView,DetailsCategoriesView

urlpatterns = [
path('<int:pk>/edit/',TaskUpdateView.as_view(), name='task_edit'),
path('<int:pk>/',TaskDetailView.as_view(), name='task_detail'),
path('<int:pk>/delete/',TaskDeleteView.as_view(), name='task_delete'),
path('new/', TaskCreateView.as_view(), name='task_new'),
path('categories/', CategoriesView.as_view(), name='categories'),
path('<int:pk>/categories/', DetailsCategoriesView.as_view(), name='categories_details'),
path('', TaskListView.as_view(), name='task_list'),
]