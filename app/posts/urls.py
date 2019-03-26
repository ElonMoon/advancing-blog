from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list),
    path('create/', views.post_create),
    path('<int:post_id>/', views.post_detail, name='detail'),
    path('<int:post_id>/edit/', views.post_update, name='update'),
    path('delete/', views.post_delete),
]
