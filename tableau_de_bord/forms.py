# forms.py

from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'quantity')
        labels = {
            'name': 'Nom du Produit',
            'category': 'Catégorie',
            'quantity': 'Quantité',
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'order_quantity')
        labels = {
            'product': 'Produit',
            'order_quantity': 'Quantité de Commande',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit order quantity based on available product quantity
        product = self.initial.get('product')  # Get the initial product instance
        if product:
            self.fields['order_quantity'].widget.attrs['max'] = product.quantity
