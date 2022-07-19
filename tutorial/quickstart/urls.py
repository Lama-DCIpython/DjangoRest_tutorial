from django.urls import path
from tutorial.quickstart import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
]
