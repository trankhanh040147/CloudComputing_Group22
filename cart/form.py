from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(label='Số lượng',choices=PRODUCT_QUANTITY_CHOICES, coerce=int) # Quantity -> so luong
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
