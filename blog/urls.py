from django.urls import path
from . import views    #. eshte per te treguar folderin ne te cilin ndodhemi


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]