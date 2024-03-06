
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.db.models import Q

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'item_details.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ItemForm()
    return render(request, 'createItem.html', {'form': form})

def item_edit(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('itemlist')
    else:
        form = ItemForm(instance=item)
    return render(request, 'createItem.html', {'form': form})

def item_delete(request, pk):
    task=Item.objects.get(pk=pk).delete()
    return redirect('itemlist')


def search(request):
    if 'keyword' in request.GET:
        keyword= request.GET['keyword']
        if keyword:
            item= Item.objects.filter(title__icontains=keyword)
    return render (request, 'items.html', {'item': item})

