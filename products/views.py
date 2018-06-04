from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Products
# from __future__ import print_function


class IndexView(generic.ListView):
    template_name = "products/index.html"
    context_object_name = 'products_list'

    def get_queryset(self):
        return Products.objects.filter().order_by('-id')


class AddprodcutView(generic.ListView):
    model = Products
    template_name = "products/addproduct.html"


def insertProduct(request):
    if request.method == "POST":
        try:
            proname = request.POST['proname']
            protype = request.POST['protype']
            proquantity = request.POST['proquantity']
            q = Products(product_name=proname,
                         product_type=protype, quantity=proquantity)
            q.save()
        except:
            print("exception")
    return redirect('/products')
    # return HttpResponseRedirect(reverse('products:index'))


def editProduct(request, product_id):
    pro = Products.objects.get(id=product_id)
    return render(request, 'products/addproduct.html', {'products': pro})


def updateProduct(request):
    if request.method == "POST":
        try:
            proid = request.POST['proid']
            proname = request.POST['proname']
            protype = request.POST['protype']
            proquantity = request.POST['proquantity']
        except:
            print("exception")
    Products.objects.filter(id=proid).update(
        product_name=proname, product_type=protype, quantity=proquantity)
    return redirect('/products')
    # return HttpResponseRedirect(reverse('products:index'))


def deleteProduct(request, product_id):
    q = Products.objects.get(id=product_id)
    q.delete()
    return HttpResponseRedirect(reverse('products:index'))


class GameView(generic.ListView):
    model = Products
    template_name = "products/game.html"