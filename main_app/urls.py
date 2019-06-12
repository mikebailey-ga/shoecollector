from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes_index, name='shoes'),
    path('shoes/<int:shoe_id>/', views.shoes_detail, name='detail'),
]