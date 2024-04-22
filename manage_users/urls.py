from django.urls import path
from . import views

app_name = 'manage_users'
urlpatterns = [
    path('login/', views.user_login, name = 'login'),
    path('register/', views.sign_up, name ='register'),
    path(
        'authenticate_user/',
        views.authenticate_user,
        name='authenticate_user'
    ),
]