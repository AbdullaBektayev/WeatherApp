from django.urls import path
from . import views

urlpatterns = [
    path('',views.index), # url to calling function from views.py for main page
    path('<int:pk>',views.city_delete,name = 'city_delete'), # url to calling function from views.py for deleting city from database
    path('delete_all',views.city_delete_all,name= 'city_delete_all') # url to calling function from views.py for deleting all city from database
]