from django.urls import path
from .views import (
    OrderCreateView, OrderListView, AllOrdersListView,
    OrderDetailView, OrderCancelView
)

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create-order'),
    path('my-orders/', OrderListView.as_view(), name='user-orders'),
    path('all/', AllOrdersListView.as_view(), name='all-orders'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/cancel/', OrderCancelView.as_view(), name='cancel-order'),
]
