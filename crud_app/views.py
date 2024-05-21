from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.shortcuts import redirect

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product': product})

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form': form})


    return render(request,'create.html')
    
def update(request):
    product = Product.objects.all()
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        product = Product.objects.get(pk=product_id)
        product.name = name
        product.description = description
        product.price = price
        if image:
            product.image = image
        product.save()
        return redirect('update')

    context={
        'product':product
    }
    return render(request,'update.html',context)

def delete(request):
    products = Product.objects.all()
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_to_delete = Product.objects.get(pk=product_id) 
        product_to_delete.delete()
        return redirect('delete')
    
    context = {
        'products': products
    }
    return render(request, 'delete.html', context)
