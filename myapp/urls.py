from django.urls import path
from myapp import views


urlpatterns = [
    path("category_api/", views.CategoryListCreateView.as_view(), name="category_api"),
    path("category_api/<int:pk>/", views.CategoryRUDView.as_view(), name="category_rud_api"),
    path("product_api/", views.ProductListCreateView.as_view(), name="product_api"),
    path("product_api/<int:pk>/", views.ProductRUDView.as_view(), name="product_rud_api"),
    

    
]
