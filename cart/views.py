from django.shortcuts import render

# Create your views here.
def cart_summary(request):
    return render(request, 'cart_summary.html', {})


def cart_add(request, product_id):
    pass

def cart_delete(request, product_id):
    pass

def cart_update(request):
    pass