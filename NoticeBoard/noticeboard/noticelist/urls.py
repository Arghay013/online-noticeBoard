from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_notice/', views.add_notice, name='add_notice'),
    path('delete_notice/<int:notice_id>/', views.delete_notice, name='delete_notice'),
]
