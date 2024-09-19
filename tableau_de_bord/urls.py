from django.urls import path
from . import views 

urlpatterns = [
    path('dashboard/', views.index, name='tableau_de_bord-index'),
    path('staff/', views.staff, name='tableau_de_bord-staff'),
    path('staff/detail/<int:pk>', views.staff_detail, name='tableau_de_bord-staff-detail'),
    path('product/', views.product, name='tableau_de_bord-product'),
    path('product/delete/<int:pk>/', views.product_delete, name='tableau_de_bord-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='tableau_de_bord-product-update'),
    path('order/', views.order, name='tableau_de_bord-order'),




]