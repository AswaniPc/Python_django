from django.shortcuts import render , get_object_or_404
from .models import *
from django.contrib.auth.models import User
# Create your views here. 
def home(request):
	categorys=Category.objects.all()
	products = Product.objects.all().order_by('-timestamp')[:3]
	#productimage = ProductImage.objects.all().filter(featured=True)[:3]
	for product in products:
		product.productimage = product.productimage_set.all()

	p = Product.objects.all()
	for pdt in p:
		pdt.productimage = pdt.productimage_set.all().filter(featured=True)[:3]

	template = 'home.html'	
	return render(request, template,{'categorys':categorys, 'products':products ,'p':p})

def about(request):
	categorys=Category.objects.all()
	template = 'about.html'
	return render(request,template,{'categorys':categorys})

def contact(request):
	categorys=Category.objects.all()
	template = 'contact.html'
	return render(request,template,{'categorys':categorys})

def subcategory(request, slug):
	categorys=Category.objects.all()
	subcategory = Subcategory.objects.get(slug=slug)
	product = Product.objects.filter(sub_category=subcategory)
	context = {'categorys':categorys,'subcategory': subcategory,'product':product}
	template = 'products/subcategory.html'	
	return render(request, template, context)

def single(request, slug):
	categorys=Category.objects.all()
	product = Product.objects.get(slug=slug)
	#images = product.productimage_set.all()
	images = ProductImage.objects.filter(product=product)
	context = {'categorys':categorys,'product': product, "images": images}
	template = 'products/single.html'	
	return render(request, template, context)
	

