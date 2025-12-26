from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('register/', views.register_page, name='restaurant-register'), 
    path('login/', views.login_page, name='restaurant-login'),
    path('logout/', views.logout_page, name='restaurant-logout'),

]
