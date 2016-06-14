from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from decimal import Decimal
from django.conf import settings

from accounts.models import UserAddress
from carts.models import Cart


STATUS_CHOICES = (
		("Started", "Started"),
		("Abandoned", "Abandoned"),
		("Finished", "Finished"),
	)

try:
	tax_rate = settings.DEFAULT_TAX_RATE
except Exception, e:
	print str(e)
	raise NotImplementedError(str(e))

class Order(models.Model):
	user = models.ForeignKey(User,null=True, blank=True)
	order_id = models.CharField(max_length=120, default='ABC', unique=True)
	cart = models.ForeignKey(Cart)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
	#shipping_address = models.ForeignKey(UserAddress, related_name='shipping_address',default=1)
	#billing_address = models.ForeignKey(UserAddress, related_name='billing_address',default=1)
	sub_total = models.DecimalField(default=10.99, max_digits=10, decimal_places=1)
	tax_total = models.DecimalField(default=0.00, max_digits=10, decimal_places=1)
	final_total = models.DecimalField(default=10.99, max_digits=10, decimal_places=1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.order_id

	def get_final_amount(self):
		instance = Order.objects.get(id=self.id)
		two_places = Decimal(10) ** -2
		tax_rate_dec = Decimal("%s" %(tax_rate))
		sub_total_dec = Decimal(self.sub_total)
		tax_total_dec = Decimal(tax_rate_dec * sub_total_dec).quantize(two_places)
		instance.tax_total = tax_total_dec
		instance.final_total = sub_total_dec + tax_total_dec
		instance.save()
		return instance.final_total