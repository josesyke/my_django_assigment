from django.urls import path
from . import views


urlpatterns = [
  
    path('', views.send_message, name='send_message'),
    path('send_message/', views.send_message, name='send_message'),
    # path('send_test_email/', views.send_test_email, name='send_test_email'),
]
