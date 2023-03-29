from django.urls import path
from .views import ListNewUser, DetailNewUser

urlpatterns = [
    path("<int:pk>/", DetailNewUser.as_view(), name="todo_detail"),
    path("", ListNewUser.as_view(), name="todo_list"),
]