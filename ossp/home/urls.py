from django.urls import path, re_path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('chat/',views.process_url, name='process'),
    path('<int:user_id>/', views.home_v, name='homepage'),
    path('<int:user_id>/question_send/', views.question_send_initial, name='question_send_initial'),
    path('<int:user_id>/<int:chatroom_id>/', views.chat_v, name='chatpage'),
    path('<int:user_id>/<int:chatroom_id>/question_send/', views.question_send, name='question_send'),
    path('<int:user_id>/room_delete/<int:del_id>/', views.room_delete, name='room_delete'),
    path('test/', views.test, name='test')
]
