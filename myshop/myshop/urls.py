"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    (?P<title>(\d+))/$
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from products import views as products_views
from accounts import views as accounts_views
from carts import views as carts_views
from orders import views as orders_views

urlpatterns = [
    url(r'^$',products_views.home,name='home'),
    url(r'^home/$',products_views.home,name='home'),
    url(r'^about/$',products_views.about,name='about'),
    url(r'^contact/$',products_views.contact,name='contact'),

    #url(r'^products/$', products.views.all, name='all'),
    url(r'^products/(?P<slug>[-\w]+)/$',products_views.single, name='single'),
    url(r'^products/(?P<slug>[-\w]+)/$',products_views.subcategory, name='subcategory'),

    url(r'^cart/(?P<id>\d+)/$', carts_views.cart_remove, name='cart_remove'),
    url(r'^cart/(?P<slug>[\w-]+)/$', carts_views.cart_add, name='cart_add'),
    url(r'^cart/$', carts_views.cart, name='cart'),

    url(r'^checkout/$', orders_views.checkout, name='checkout'),
    url(r'^orders/$', orders_views.orders, name='orders'),

    url(r'^login/$',accounts_views.login,name='login'),
    url(r'^logout/$',accounts_views.signout, name='logout'),
    url(r'^register/$',accounts_views.register,name='register'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', accounts_views.activation, name='activation'),
    url(r'^accounts/add_address/$', accounts_views.add_address, name='add_address'),

    
    url(r'^admin/', admin.site.urls),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''
 