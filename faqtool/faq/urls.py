from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_list, name='faq_list'),
    path('create/', views.create_question, name='create_question'),
    path('edit/<int:id>/', views.edit_question, name='edit_question'),
    path('delete/<int:id>/', views.delete_question, name='delete_question'),
    path('faq_script/', views.faq_script, name='faq_script'),
]
