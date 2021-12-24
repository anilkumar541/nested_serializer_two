
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from myapp.models import Category, Product
from myapp.serializers import CategorySerializer, ProductSerializer

class CategoryListCreateView(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductListCreateView(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductRUDView(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



#  def update(self, instance, validated_data):
    #     category_data=validated_data.pop('category')
    #     categories=(instance.category).all()
    #     categories=list(categories)
    #     instance.product_name=validated_data.get('product_name', instance.product_name)
    #     instance.created_at=validated_data.get('created_at', instance.created_at)
    #     instance.updated_at=validated_data.get('updated_at', instance.updated_at)
    #     instance.save()
    #     for category_dt in category_data:
    #         category=categories.pop(0)
    #         category.category_name=category_dt.get('category_name', category.category_name)
    #         category.created_at=category_dt.get('created_at', category.created_at)
    #         category.updated_at=category_dt.get('updated_at', category.updated_at)
    #         category.save()
    #     return instance    
