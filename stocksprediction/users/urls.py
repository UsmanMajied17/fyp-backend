from django.urls import path, include
from users import views


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),

    path('', views.UsersView.as_view({
        'post': 'create',
        'get': 'list',
    })),

    path('<int:pk>/', views.UsersView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]