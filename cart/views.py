from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    # Get the products in the cart
    cart_products = cart.get_prods()
    return render(request, 'cart_summary.html', {"cart_products": cart_products})


def cart_add(request):
    # Get the cart 
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        # Get Stuff
        product_id = int(request.POST.get('product_id'))
        # lockup product in DB
        product = get_object_or_404(Product, id=product_id)
        # Save to session
        cart.add(product=product)

        # Return response
        response = JsonResponse({'Product Name: ': product.name})
        return response

def cart_delete(request, product_id):
    pass

def cart_update(request):
    pass