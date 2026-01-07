from django.urls import path
from . import views


urlpatterns = [
    path('menu-items', views.MenuItemListView.as_view()),
    path('menu-items/<int:pk>', views.MenuItemDetailView.as_view()),
    path('categories', views.CategoryListView.as_view()),
    path('cart/menu-items', views.CartListView.as_view()),
    path('cart/menu-items/<int:pk>', views.CartDetailView.as_view()),
    path('orders', views.OrderListView.as_view()),
    path('orders/<int:pk>', views.OrderDetailView.as_view()),
    path('groups/manager/users', views.ManagerUsersView.as_view()),
    path('groups/manager/users/<int:pk>', views.ManagerUserDetailView.as_view()),
    path('groups/delivery-crew/users', views.DeliveryCrewUsersView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.DeliveryCrewUserDetailView.as_view()),
]