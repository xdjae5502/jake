from django import forms
from .models import Product, Battery, WatchPart

class BatteryForm(forms.ModelForm):
    class Meta:
        model = Battery
        fields = ['name', 'price', 'digital', 'image']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'digital', 'image']

class WatchPartForm(forms.ModelForm):
    class Meta:
        model = WatchPart
        fields = ['name', 'description', 'price', 'image']