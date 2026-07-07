from django.urls import path
from . import views

urlpatterns = [
    # The name='login' matches redirect('login')
    path('', views.login_page, name='login'), 
    
    # The name='home' matches redirect('home')
    path('home/', views.home, name='home'),   
    
    path('logout/', views.logout_page, name='logout'),
]