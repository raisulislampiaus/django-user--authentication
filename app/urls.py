from django.urls import path


from . import views

urlpatterns = [
     path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name='route'),
    path('users/register/', views.userRegister, name='register'),
    path('users/profile/', views.getUser, name='users-profile'),
    path('users/', views.getUsers, name='users'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>/', views.getProduct, name='product'),
]
