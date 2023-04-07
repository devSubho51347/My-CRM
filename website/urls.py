from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('login/',views.login_user, name = 'login_user'),
    path('logout/',views.logout_user,name = 'logout_user'),
    path('register/',views.register_user, name = 'register_user'),
    path('delete/<int:pk>', views.delete_task, name = 'delete_task'),
    path('addTask/', views.add_task, name = "add_task"),
    path('update/<int:pk>', views.update_task, name = "update_task"),
]
