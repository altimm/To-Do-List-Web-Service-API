from django.urls import path
from django.contrib import admin
#now import the views.py file into this code
from . import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path('create/', views.create_view),
    path('', views.retrieve_view),
    path('complete/', views.update_view),
    path('delete/', views.delete_view),
]