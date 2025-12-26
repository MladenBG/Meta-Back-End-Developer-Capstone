from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

# Router for BookingViewSet
router = DefaultRouter()
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    # Restaurant app routes
    path('restaurant/', include('restaurant.urls')),

    # Menu API endpoints (generic views)
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu-list'),
    path('api/menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),

    # Booking API via router
    path('api/', include(router.urls)),

    # Djoser authentication endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # DRF token auth
    path('api-token-auth/', obtain_auth_token),
]
