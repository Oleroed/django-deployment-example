from django.urls import path
from basic_app import views


app_name = 'basic_app'


urlpatterns= [
    path('relative/', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('other/', views.other, name='other'),
]