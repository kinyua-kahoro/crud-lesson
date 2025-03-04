from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.user_list),
    path('Add/', views.add_user),
    path('Edit/<id>/', views.Edituser),
    path('Delete/<eid>/', views.Deleteuser),
    path('View/<eid>/', views.Viewuser),
]