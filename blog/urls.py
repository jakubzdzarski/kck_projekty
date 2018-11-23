from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='nonsense'),
    path('mybio/', views.mybio, name='mumble'),
    path('myblog/', views.myblog, name='gibberish'),
]
