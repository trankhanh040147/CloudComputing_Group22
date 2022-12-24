from django.shortcuts import render
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/login/')
def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		current_user = request.user
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			data = Order()
			data.customer = current_user
			data.first_name = form.cleaned_data['first_name']
			data.last_name = form.cleaned_data['last_name']
			data.email = form.cleaned_data['email']
			data.address = form.cleaned_data['address']
			data.postal_code = form.cleaned_data['postal_code']
			data.city = form.cleaned_data['city']
			data.ip = request.META.get('REMOTE_ADDR')
			data.save()
			for item in cart:
				OrderItem.objects.create(
					order=data,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity']
				)
			cart.clear()
		return render(request, 'orders/created.html', {'order': data})
	else:
		form = OrderCreateForm()
	return render(request, 'orders/create.html', {'form': form})
