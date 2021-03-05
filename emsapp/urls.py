from django.urls import path

from .views import *
urlpatterns = [
    path('logout', user_logout, name='user_logout'),
    path('add-employee', add_employee, name='add_employee'),
    path('add-todo-list', add_todo_list, name='add_todo_list'),
    
    path('', user_login, name='user-login'),
    
    path('todo-ist-evaluation/<int:id>/<sts>', todo_list_evaluation, name='todo-list-evaluation'),


    path('application-approval/<int:id>/<sts>', application_approval, name='application_approval'),

    path('all-application', all_application, name='all_application'),
    path('userprofile', user_profile, name='user_profile'),
    path('add-leaveform', add_leave_form, name='add-leave-form'),
    
    path('todolist', to_do_list, name='todolist'),
]
