from rest_framework import serializers,status,generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, OrderItem
from products.models import Product
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'is_paid', 'items']
        read_only_fields = ['user', 'created_at', 'is_paid']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']

            # Reduce product stock
            if product.stock < quantity:
                raise serializers.ValidationError(
                f"Not enough stock for {product.name}. Available: {product.stock}"
                )   

            product.stock -= quantity
            product.save()

            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        return order


        

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensures a user can only fetch their own orders
        return Order.objects.filter(user=self.request.user)

class AllOrdersListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderCancelView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            order = Order.objects.get(pk=pk, user=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        if order.is_paid:
            return Response({"error": "Paid orders cannot be cancelled"}, status=400)

        order.delete()
        return Response({"message": "Order cancelled"}, status=204)