from .models import MenuItem, Category, Cart, Order, OrderItem
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer, OrderSerializer, OrderItemSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework.pagination import PageNumberPagination

class MenuItemListView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    pagination_class = PageNumberPagination
    page_size = 3
    ordering = ['-price']
    search_fields = ['title', 'category__title']
    filter_fields = ['category']

class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    ordering = ['-price']
    search_fields = ['title', 'category__title']
    filter_fields = ['category']

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    ordering = ['title']
    search_fields = ['title']
    filter_fields = ['title']

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    ordering = ['title']
    search_fields = ['title']
    filter_fields = ['title']

class CartListView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    ordering = ['quantity']
    search_fields = ['menuitem__title']
    filter_fields = ['menuitem__category']
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        """Delete all cart items for the current user"""
        cart_items = self.get_queryset()
        count = cart_items.count()
        cart_items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    ordering = ['quantity']
    search_fields = ['menuitem__title']
    filter_fields = ['menuitem__category']
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)



class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    pagination_class = PageNumberPagination
    page_size = 3
    ordering = ['date']
    search_fields = ['user__username']
    filter_fields = ['user__username']

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    ordering = ['date']
    search_fields = ['user__username']
    filter_fields = ['user__username']

class ManagerUsersView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    
    def get_queryset(self):
        try:
            manager_group = Group.objects.get(name='Manager')
            return User.objects.filter(groups=manager_group)
        except Group.DoesNotExist:
            return User.objects.none()

class ManagerUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    
    def get_queryset(self):
        return User.objects.filter(groups=Group.objects.get(name='Manager'))

class DeliveryCrewUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    
    def get_queryset(self):
        return User.objects.filter(groups=Group.objects.get(name='Delivery Crew'))

class DeliveryCrewUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]