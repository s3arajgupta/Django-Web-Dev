from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:blog_id>/edit', views.edit, name='edit'),
    path('<int:blog_id>', views.detail, name='detail'),
]
