from django.urls import path
from . import views

urlpatterns =[
    path('',views.list_todo_items),
    path('<int:db_id>',views.list_todo_items_target),
    path('insert_todo/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_todo_item'),
    path('<int:db_id>/insert_todo/',views.insert_todo_item_target,name='insert_todo_item'),
    path('<int:db_id>/delete_todo/<int:todo_id>/',views.delete_todo_item_target,name='delete_todo_item'),    
]