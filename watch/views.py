from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Battery, WatchPart
from .forms import ProductForm,BatteryForm,WatchPartForm

def edit_part(request, part_id):
    part = get_object_or_404(WatchPart, id=part_id)
    if request.method == 'POST':
        form = WatchPartForm(request.POST, request.FILES, instance=part)
        if form.is_valid():
            form.save()
            return redirect('watch_parts')
    else:
        form = WatchPartForm(instance=part)

    return render(request, 'pages/edit_part.html', {'form': form, 'part': part})

def delete_part(request, part_id):
    part = get_object_or_404(WatchPart, id=part_id)
    if request.method == 'POST':
        part.delete()
        return redirect('watch_parts')
    
    return render(request, 'pages/delete_part.html', {'part': part})

def watch_parts(request):
    
    parts_data = WatchPart.objects.all()
    return render(request, 'pages/parts.html', {'parts_data': parts_data})

def add_parts(request):
    if request.method == 'POST':
        form = WatchPartForm(request.POST, request.FILES)  # Siguruhing may "request.FILES" para sa mga imahe
        if form.is_valid():
            form.save()
            return redirect('watch_parts')  
    else:
        form = WatchPartForm()

    return render(request, 'pages/add_parts.html', {'form': form})


def our_story(request):
    return render(request, 'pages/About.html')

def store_location(request):
    return render(request, 'pages/store_location.html')

def contact(request):
    return render(request, 'pages/contact.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'pages/add_product.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('watch_page')
    else:
        form = ProductForm(instance=product)
    return render(request, 'pages/edit_watch.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('watch_page')
    return render(request, 'pages/delete_watch.html', {'product': product})

def edit_battery(request, battery_id):
    battery = get_object_or_404(Battery, id=battery_id)
    
    if request.method == 'POST':
        form = BatteryForm(request.POST, instance=battery)
        if form.is_valid():
            form.save()
            return redirect('Batteries')
    else:
        form = BatteryForm(instance=battery)
    
    return render(request, 'pages/edit_battery.html', {'form': form, 'battery': battery})

def delete_battery(request, battery_id):
    battery = get_object_or_404(Battery, id=battery_id)
    
    if request.method == 'POST':
        battery.delete()
        return redirect('Batteries')
    
    return render(request, 'pages/delete_battery.html', {'battery': battery})

def Index(request):
    context = {}
    return render(request, "pages/Index.html")

def Batteries(request):
    batteries = Battery.objects.all()
    return render(request, 'pages/Batteries.html', {'batteries': batteries})


def watch_page(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('watch_page')

    return render(request, 'pages/Watch.html', {'form': form, 'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('watch_page')  # Redirect to the watch page after adding a product
    else:
        form = ProductForm()

    return render(request, 'pages/add_product.html', {'form': form})

def add_battery(request):
    if request.method == 'POST':
        form = BatteryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Batteries')  # Redirect to the battery page after adding a battery
    else:
        form = BatteryForm()

    return render(request, 'pages/add_battery.html', {'form': form})


