from django.urls import path
from . import views

urlpatterns = [
    path("index",views.index, name='index'),


    path('',views.login_page,name='login'),
    path("logout/",views.logout_user,name="logout"),
    path('register/',views.new_register,name='register'),


    path("create-product/", views.create, name="create" ),
    path('update/<int:pk>/',views.update, name='update'),
    path('delete/<int:pk>/',views.delete, name='delete'),


]
