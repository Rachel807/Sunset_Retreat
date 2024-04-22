from django.urls import path, include
from . import views

app_name = 'home_page'
urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('detail/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('view/<int:pk>/', views.RoomView.as_view(), name = 'room_info')
]