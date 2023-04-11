from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('t', views.teachers_info),
    path('forms',views.showFrom)

]