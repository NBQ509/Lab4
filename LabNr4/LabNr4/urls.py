from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include("firstApplication.urls")),
    path('<int:number>',include("firstApplication.urls")),
    path('taxrate/',include("firstApplication.urls"))


]
