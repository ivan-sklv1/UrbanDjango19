from django.urls import path
from task1 import views


app_name = 'task1'

urlpatterns = [
    path('', views.main),
    path('games/', views.games_list),
    path('cart/', views.cart_list),
]
