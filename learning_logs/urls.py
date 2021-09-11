"""defines url patterns for our app learning logs"""

from django.urls import path
# from django import
from django.urls.conf import include 
from . import views

app_name = 'learning_logs'

urlpatterns=[

    
    #home page
    path('',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    # page for adding a new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    #page for editing existing entry
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),

    
]
