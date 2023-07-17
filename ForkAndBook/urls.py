from django.urls import path
from .import views

urlpatterns = [
    path("", views.registerpage, name="registerpage"),
    path("registerpage2", views.registerpage2, name="registerpage2"),
    path("loginpage/",views.loginpage, name="loginpage"),
    path("loginpage2/",views.loginpage2, name="loginpage2"),
    path("homeStudent/",views.homeStudent,name="homeStudent"),
    path("homeEmployee/", views.homeEmployee, name="homeEmployee"),
    path("homeEmployee/registerMenu/", views.registerMenu, name="registerMenu"),
    path('studentUpdate/', views.studentUpdate, name='studentUpdate'),
    path('employeeUpdate', views.employeeUpdate, name='employeeUpdate'),
    path('studentDelete/', views.studentDelete, name='studentDelete'),
    path('employeeDelete/', views.employeeDelete, name='employeeDelete'),
    path('choosepage/', views.choosepage, name='choosepage'),
    path('BigCubeMenu/', views.BigCubeMenu, name='BigCubeMenu'),
    path('KhemahBiruMenu/', views.KhemahBiruMenu, name='KhemahBiruMenu'),
    path('addFood/<str:menu_id>/', views.addFood, name='addFood'),
    path('deleteFood/<int:food_id>/', views.deleteFood, name='deleteFood'),
    path('deleteMenu/<str:menu_id>/', views.deleteMenu, name='deleteMenu'),
    path('approveFood/<int:food_id>/', views.approveFood, name='approveFood'),
    path('rejectFood/<int:food_id>/', views.rejectFood, name='rejectFood'),

]